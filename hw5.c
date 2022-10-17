#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int bit(int num)
{
	if (num < 2)
	{
		printf("1");
		return 0;
	}
	else
	{
		bit(num / 2);
		printf("%d", num % 2);
	}
}
int main(void)
{
	int num;
	printf("양의 정수 입력: ");
	scanf("%d", &num);
	bit(num);
	return 0;
}