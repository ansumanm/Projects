#include<unistd.h> /* access() */
#include<stdio.h> /* printf() */
#include<stdlib.h> /* exit() */

#define DIRNAME "./"
#define FILE_1 "test*"
#define FILE_2 "testing"
#define FILE_3 "*test*"

void print_usage(char *argv[])
{
	printf("Usage: \n");
	printf("%s <path>\n",argv[0]);
}

/* access() cant test wild cards. */
/* stat() */
int main(int argc, char *argv[])
{
	int rc;
	char filename[256];

	if (argc == 1)
	{
		print_usage(argv);
		exit(0);
	}

	printf("Testing access of %s\n",argv[1]);
	rc = access(argv[1],F_OK);
	if (rc == -1)
	{
		perror("File not found:");
	}

	if (rc == 0)
	{
		printf("File found.\n");
	}

	snprintf(filename,256,"%s%s",DIRNAME,FILE_1);
	printf("Testing access of %s\n",DIRNAME FILE_2);

	rc = access(DIRNAME FILE_2,F_OK);

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
