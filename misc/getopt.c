#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int
main(int argc, char *argv[])
{
	int j;
	int c;
	int opt;

	while ((opt = getopt(argc, argv, "jcf:")) != -1) {
		switch (opt) {
			case 'j':
				j = 1;
				printf("Option j\n");
				break;
			case 'c':
				printf("Option c\n");
				break;
			case 'f':
				printf("Option f %s\n",optarg);
				break;
			default: /* '?' */
				exit(EXIT_FAILURE);
		}
	} 

	printf("Action %s\n",argv[argc -1]);
	exit(EXIT_SUCCESS);
}

