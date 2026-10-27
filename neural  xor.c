#include <stdio.h>
#include <conio.h>
int activation(float sum)
{
    if (sum >= 0) return 1;
    else return 0;
}
int main()
{
    clrscr();
    int x1, x2, h1, h2, output;
    printf("enter x1 and x2 (either 0 or 1):");
    scanf("%d%d", &x1, &x2);
    h1 = activation(x1 + x2 - 0.5);
    h2 = activation(-x1 - x2 + 1.5);
    output = activation(h1 + h2 - 1.5);
    printf("\nHidden layer h1 (OR) = %d", h1);
    printf("\nHidden layer h2 (NAND) = %d", h2);
    printf("\nXOR Output = %d", output);
    getch();
    return 0;
}