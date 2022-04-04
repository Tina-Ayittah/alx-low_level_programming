#include <string.h>
#include <stdio.h>

int main () {
   char str[80] = "This is - www.tutorialspoint.com - website";
   const char s[2] = "-";
   const char t[2] = " ";
   char *token;

   /* get the first token */


   /* walk through other tokens */
   while( token != NULL ) {
      printf( " %c\n", *token );

      token = strtok(NULL, s, t);


   }

   return(0);
}
