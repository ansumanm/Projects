#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

int main(int argc, char *argv[])
{
	char **cptr = NULL;
	int count = 0;
	int opt;
	int i;

	while ((opt = getopt(argc, argv, "e:")) != EOF)
	{
		switch(opt) {
			case 'e':
				cptr = realloc(cptr,(sizeof(char *) * (count + 1)));
				if (cptr == NULL) exit(1);
				cptr[count++] = strdup(optarg);
				break;
			default:
				break;
		}
	}

	for(i = 0; i<count; i++)
	{
		printf("cptr[%d] = %s\n",i,cptr[i]);
		free(cptr[i]);
	}

	return 0;
}
