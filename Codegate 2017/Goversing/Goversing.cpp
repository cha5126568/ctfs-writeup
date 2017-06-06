#include<stdio.h>
#include<stdlib.h>
#include<iostream>
char off_5167C0[] = "encryptk";
void main_decrypt(unsigned char* v23, unsigned __int64 a8)
{
   FILE *fp2=fopen("output.jpg","wb");
    __int64 v10 = 0LL;
  __int64 v11 = 4LL;
   __int64 v16 = 0LL;
  char *a7 = (char *)calloc(a8 , sizeof(__int64));
  for ( __int64 k = 0LL; k < (signed __int64)a8; ++k )
  {
    v23 [k] ^= off_5167C0[k % -4];
  }
  __int64 v20 = a8 - 1;
  for ( __int64 j = 0LL; (signed __int64)a8 / 2 - 1 > j; ++j )
  {
    v23[v20--] ^= v23 [j];
  }
       do
    {
      std::swap(v23[v16],v23[v16 + 4]);
      std::swap(v23[v16+1],v23[v16 + 5]);
      std::swap(v23[v16+2],v23[v16 + 6]);
      std::swap(v23[v16+3],v23[v16 + 7]);
      v16 += 8LL;
    }
    while ( (signed __int64)(a8 - 8) > (signed __int64)v16 );

  for ( __int64 i = 0LL; i < (signed __int64)a8; ++i )
  {
    v23[i] ^= off_5167C0[i % -8];
  }
  do
  {
      a7[v11] = v23[v11] ^ v23[v11 - 4];
      a7[v11 + 1] = v23[v11+1] ^ v23[v11 - 3];
      a7[v11 + 2] = v23[v11+2] ^ v23[v11 - 2];
      a7[v11 + 3] = v23[v11+3] ^ v23[v11 - 1];
      v11 += 4LL;
  }
  while ( (signed __int64)v11 < (signed __int64)a8 );
    do
  {
    a7[v10] = v23[v10];
    ++v10;
  }
  while ( (signed __int64)v10 < 4 );

  for(int i=0;i<11616;i++)
  {
     fprintf(fp2,"%c",a7[i]);
  }
}

int main(void)
{
   FILE *fp=fopen("flag.encrypt","rb");
   unsigned char buf[11616];
   fread(buf,1,11616,fp);
   main_decrypt(buf,11616);
}