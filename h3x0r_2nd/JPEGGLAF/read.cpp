#include<stdio.h>
#include<windows.h>
int main(void)
{
	FILE *fp=fopen("temp.bin","rb");
	FILE *fp2=fopen("test.bin","wb");
	char buf[8356];
	fread(buf,1,8356,fp);
	for(int i=8355;i>=0;i--)
	{
		fprintf(fp2,"%c",buf[i] & 0xff);
	}
}
