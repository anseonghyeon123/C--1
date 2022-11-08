#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{
	int num[5], i;
	printf("Please input five integers: ");
	scanf("%d", &num[0]);
	for (i = 1; i < 5; i++)
		scanf("%d", &num[i]);
	printf("\nOdd numbers : ");
	for (i = 0; i < 5; i++)
	{
		if (num[i] % 2 != 0)
			printf("%d ", num[i]);
	}
	printf("\nEven numbers: ");
	for (i = 0; i < 5; i++)
	{
		if (num[i] % 2 == 0)
			printf("%d ", num[i]);
	}
	return 0;
} 
