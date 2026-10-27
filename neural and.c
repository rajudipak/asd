#include <stdio.h>
#include <conio.h>
int main()
{
    clrscr();
    float x1, x2, sum;
    int output = 0;
    printf("enter x1 and x2:");
    scanf("%f%f", &x1, &x2);
    sum = x1 + x2 - 1.5;
    if (sum >= 0) output = 1;
    printf("sum = %.2f\noutput = %d", sum, output);
    getch();
    return 0;
}