#include<stdio.h>
#include<string.h>
#include <boost/uuid/sha1.hpp>

boost::uuids::detail::sha1 s;

int main()
{
	//0xff -> unknown
	char arr[] = { 0x48,0x33,0x58,0x30,0x52,0x7B,0x32,0x65,0x56,0x33,0x72,0x35,0x45,0x5F,0x31,0x44,0x65,0x34,0x5F,0x57,0x31,0x37,0x48,0x5F,0x43,0xff,0xff,0xff,0xff,0xff,0x7D };
	unsigned char tmparr[] = { 0x14,0x4c,0x5e,0xe2,0x27 };
	int i;
	for (int a = 32;a <= 127;a++)
	{
		printf("first char : %c\n", a);
		for (int b = 32;b <= 127;b++)
		{
			for (int c = 32;c <= 127;c++)
			{
				for (int d = 32;d <= 127;d++)
				{
					for (int e = 32; e <= 127;e++)
					{
						arr[25] = a;
						arr[26] = b;
						arr[27] = c;
						arr[28] = d;
						arr[29] = e;

						s.reset();
						s.process_bytes(arr, 31);
						unsigned int digest[5];
						s.get_digest(digest);
						for (i = 0;i < 5;i++)
						{
							if ((digest[i] & 0xff) != tmparr[i]) break;
						}
						if (i == 5)
						{
							printf("ANSWER : %c%c%c%c%c\n", a, b, c, d, e);
						}
					}
				}
			}
		}
	}
	return 0;
}
