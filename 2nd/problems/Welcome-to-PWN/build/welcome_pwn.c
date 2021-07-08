#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

void setup(){
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  alarm( 180 );
}
void print_flag(){
  FILE *fp;
  char flag[64];

  fp = fopen( "flag.txt", "r" );
  if( fp == NULL ){
    printf("Faild open file: flag.txt");
    exit( 1 );
  }

  fgets( flag, sizeof( flag ), fp );
  printf( "%s", flag );

  return;
}

int main(){
  char pass[255] = { 0 };

  setup();

  puts("Great!");
  puts("You connected problem server!");
  puts("Flag is here!");

  puts("");
  printf("Input password: ");
  scanf("%255s", pass );      // Input password

  if( strcmp( pass, "GAS_GAS_GAS" ) == 0 ){   // Compare input password with correct password
    puts("Congrats!");
    puts("");
    //print_flag();
    system("/bin/sh\0");    // Get shell!!
  }
  else {
    puts("Incorrect password...");
  }

  puts("Bye!");

  return 0;
}
