#include <stdio.h>
int main(void)
{
	for (int count = 1; count < 6; count++)
	{
		for (int no = 0; no < 5 - count; no++)
		{
			printf(" ");
		}
		for (int star = 1; 2 * count - 1 >= star; star++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
