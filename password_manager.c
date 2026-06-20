#include<stdio.h>
#include<string.h>


void encrypt(char pass[]){

for(int i=0;i<strlen(pass);i++){

pass[i]+=3;

}

}


int main(){


char website[50];

char password[50];



printf("Website:");

scanf("%s",website);



printf("Password:");

scanf("%s",password);



encrypt(password);



FILE *fp;


fp=fopen(
"password.txt","a"
);



fprintf(fp,
"%s : %s\n",
website,password);



fclose(fp);



printf("Password Saved");


return 0;

}