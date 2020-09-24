#!/usr/bin/python3
import sys
import os
import time
import select
import logging

# Check the arguments that we were passed
list_of_args = sys.argv
list_of_args.pop(0)

logging.basicConfig(filename='pproxy.log', format=None,  level=logging.DEBUG)

p_name = "./watch_proc"
list_of_args.insert(0, p_name)
logging.debug(str(list_of_args))

# Spawn the proxy process.
# Create a pipe and then fork. In that way, the child also gets the descriptors.

# Create two sets of pipe. One exclusively for the child process and the other for
# the parent process
parent_read_fd, child_write_fd = os.pipe()
child_read_fd, parent_write_fd = os.pipe()

if not os.fork():
    """
    Child process
    1) Dup the stdin to read descriptor
    2) Dup the stdout to write descriptor
    """
    # These descriptors will be used by the parent.
    os.close(parent_read_fd)
    os.close(parent_write_fd)

    os.dup2(child_read_fd, 0) # stdin
    os.dup2(child_write_fd, 1) # stdout
    os.dup2(child_write_fd, 2) # stderr

    # Execute the desired program
    # os.execve("/bin/bash",["/bin/bash","-c","echo stdout; echo stderr >&2"], os.environ)
    # os.execve("/bin/bash",["/bin/bash"], os.environ)
    # os.execve("/bin/cat", ["/bin/cat", "-"], os.environ)
    # os.execve("/bin/ls", ["/bin/ls"], os.environ)
    os.execve("./watch_proc", list_of_args, os.environ)
    print("Failed to exec program!")
    sys.exit(1)

# Parent Process
os.close(child_read_fd)
os.close(child_write_fd)


# Using select() we will monitor 3 descripters
# This is for reading:
# 1) sys.stdin from input from user.
# 2) parent_read_fd
# This is for writing
# 1) parent write_fd

rlist_fds = [parent_read_fd, sys.stdin]
wlist_fds = [parent_write_fd]
xlist_fds = []

in_loop = 1

while in_loop:
    """
    try:
        os.write(1, str.encode(prompt))
    except Exception as e:
        print("Write error: %s" % str(e))
        break
    """

    timeout = 1.0 # Check every 1 second if the child is alive.
    i_ready, o_ready, x_ready = select.select(rlist_fds, [], [], timeout)

    if not i_ready:
        continue

    for desc in i_ready:
        if desc == sys.stdin:
            cmd = sys.stdin.readline()
            logging.info("[-->] %s" % cmd)

            try:
                os.write(parent_write_fd, str.encode(cmd))
            except Exception as e:
                print("Parent Write error %s" % str(e))
                in_loop = False
                break

        elif desc == parent_read_fd:
            try:
                readbytes = os.read(parent_read_fd, select.PIPE_BUF)
                if len(readbytes) == 0:
                    # This implies that the child process has exited.
                    # Lets exit.
                    in_loop = False
                    break
            except Exception as e:
                print("Parent read error: %s" % str(e))
                break

            logging.info("[<--] %s" % readbytes.decode('utf-8'))

            try:
                os.write(1, readbytes)
            except Exception as e:
                print("Write error: %s" % str(e))
                in_loop = False
                break

os.close(parent_write_fd)
os.close(parent_read_fd)

# Prevent zombies!  Reap the child after exit
pid, status = os.waitpid(-1, 0)
logging.info("Child exited: pid %d returned %d"%(pid,status))
