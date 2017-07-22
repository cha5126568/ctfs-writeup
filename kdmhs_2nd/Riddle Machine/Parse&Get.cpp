#include<stdio.h>
#include<string.h>
int main(void)
{
	FILE *fp = fopen("real_data.txt", "r");
	char *p;
	char buf[1000], buf2[1000];
	char vowel[7] = "AIEOUY";
	while (!feof(fp))
	{
		fgets(buf, 1000, fp);
		memcpy(buf2, buf, 1000);
		strtok(buf, " : ");
		strtok(NULL, " ");
		while (p = strtok(NULL, " "))
		{
			int cnt = 0;
			for (int i = 0;i < 6;i++)
				if (strchr(p, vowel[i]) != NULL) cnt++;
			if (cnt == 0)
				break;
		}
		if(p == NULL)
			printf("%s", buf2);
	}
}
