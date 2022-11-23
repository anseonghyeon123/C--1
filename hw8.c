#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "math.h"
int main(void)
{
	int num[50], i;
	printf("Enter 5 real numbers: ");
	for(i=0;i<5;i++)
		scanf("%d", &num[i]);
	printf("Standard Deviation = %.3f", stand(num));
	return 0;
}