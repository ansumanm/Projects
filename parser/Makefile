# Configure the tools.
CC = gcc
CXX = g++
# LEX = flex
# YACC = bison

LDFLAGS = -ll

# all needs to be the first target.
all: example1 example2 example3 example4

# Some issue with the implicit rules.
example1.c: example1.l
example1: example1.c

example2.c: example2.l
example2: example2.c

example3.c: example3.l
example3: example3.c

example4:
	lex example4.l
	yacc -d example4.y
	$(CC) lex.yy.c y.tab.c -o example4

clean: 
	rm -f example1.c
	rm -f example2.c
	rm -f example3.c
	rm -f lex.yy.c
	rm -f y.tab.c
	rm -f y.tab.h
	rm -f example1
	rm -f example2
	rm -f example3
	rm -f example4
