#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <semaphore.h>
#include <stdio.h>

int main()
{
	mode_t mode = 0644;
	sem_t *s1 = sem_open("small",O_CREAT,mode,0);
	sem_t *s2 = sem_open("caps",O_CREAT,mode,1);
	char x = 'A';

	do {
		sem_wait(s2);
		printf("%c", x);
		fflush(stdout);
		sem_post(s1);
	} while(++x <= 'Z');

	sem_close(s2);
	sem_unlink("caps");
	return 0;
}

