%{
#include<stdio.h>
%}
%%
TEST	printf("TEST ");
#[0-9]+ printf("Test case number %d ",atoi(yytext+1));
{	printf("Open curly brace \n");
}	printf("Close curly brace \n");
Description	printf("Description ");
String		printf("String ");
Pattern		printf("Pattern ");
=		printf("equal ");
"*"		printf("%s ",yytext);
;		printf(" semi-colon\n");
%%
