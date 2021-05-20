#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){	
	int i,j,count;
	char s[100], s2[100];
				
	printf("\nDigite uma string para invertela: ");
	fgets(s, 100, stdin);
	while(s[i] != '\n'){
		count++;
		i++;
	}
	i=0;
	for(j=count-1; j>=0; j--){//invertendo a string em outra string.
		s2[i] = s[j];
		i++;
	}
	s2[count+1] = '\0';//acrescentando um fim.
	
	printf("\nString invertida: ");			
	puts(s2);
	
	system ("PAUSE");
	return 0;
}
	
