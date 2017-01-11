#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <semaphore.h>
#include <stdio.h>

/* NOTE: The named semaphores are created in /dev/shm directory. */
int main()
{
	mode_t mode = 0644;
	sem_t *s1 = sem_open("small",O_CREAT,mode,0);
	sem_t *s2 = sem_open("caps",O_CREAT,mode,1);
	char x = 'a';

	do {
		sem_wait(s1);
		printf("%c", x);
		fflush(stdout);
		sem_post(s2);
	} while(++x <= 'z');

	printf("\n");

	sem_close(s1);
	sem_unlink("small");
	return 0;
}

