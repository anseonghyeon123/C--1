#include <math.h>
double stand(int num)
{
	double sum = 0;
	int i;
	for (i = 0; i < 5; i++)
		sum += num[i];
	double aver = sum / 5;
	sum = 0;
	for (i = 0; i < 5; i++)
		sum += pow(num[i] - aver, 2);
	double sig = sqrt(sum / 5);
}