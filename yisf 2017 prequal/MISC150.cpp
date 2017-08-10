#include<stdio.h>
int main(void)
{
	unsigned char rawData[20] = {
		0x5D, 0x6D, 0x57, 0x62, 0xBF, 0x62, 0x27, 0x66, 0x0D, 0x0B, 0xB2, 0xEA,
		0xA8, 0xB8, 0xDE, 0xAB, 0xF7, 0xF0, 0xD9, 0xE3
	};
	for (int i = 0;i < 5;i++)
		printf("%c", (rawData[i] ^ 52) - 0x10);
	for (int i = 5;i < 10;i++)
		printf("%c", (rawData[i] ^ 52) + 0x20);
	for (int i = 10;i < 15;i++)
		printf("%c", (rawData[i] ^ 52) / 2);
	for (int i = 15;i < 20;i++)
		printf("%c", (rawData[i] ^ 52) ^ 0xaa);
}
