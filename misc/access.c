#include<unistd.h> /* access() */
#include<stdio.h> /* printf() */
#include<stdlib.h> /* exit() */

void print_usage(char *argv[])
{
	printf("Usage: \n");
	printf("%s <path>\n",argv[0]);
}
int main(int argc, char *argv[])
{
	int rc;

	if (argc == 1)
	{
		print_usage(argv);
		exit(0);
	}

	rc = access(argv[1],F_OK);
	if (rc == -1)
	{
		perror("File not found:");
	}

	if (rc == 0)
	{
		printf("File found.\n");
	}

	return 0;
}
