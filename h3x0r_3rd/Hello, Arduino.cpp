#include<stdio.h>
#include<string.h>
#include<stdlib.h>

const unsigned char table[32] = {
	0x7B, 0xC0, 0x68, 0x62, 0x33, 0xEC, 0x32, 0x8C, 0x35, 0x91, 0x0C, 0xB0,
	0x6F, 0xD2, 0x7B, 0xCE, 0xB3, 0xEA, 0xFD, 0x91, 0x0C, 0xB6, 0xDF, 0xE5,
	0x93, 0xCB, 0xE1, 0xDC, 0xAE, 0xA1, 0x3F, 0xA0
};
unsigned char Flag[32] = {'H','3','X','0','R','{',0};
int main(void)
{
	for (int i = 5;i < 32;i++)
		Flag[i+1] = _lrotl(Flag[i], Flag[i]&7) ^ table[i];
	printf("%s",Flag);
}
