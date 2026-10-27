
#include <stdio.h>
#include <conio.h>

void main()
{
    int x1, x2, i;
    int inputs[4][2] = {
        {0, 0},
        {0, 1},
        {1, 0},
        {1, 1}
    };
    int sum, output;

    clrscr();

    printf("AND Gate using Neural Network\n");

    for (i = 0; i < 4; i++)
    {
        x1 = inputs[i][0];
        x2 = inputs[i][1];

        sum = x1 + x2 - 1;

        if (sum > 0)
            output = 1;
        else
            output = 0;

        printf("%d %d -> %d\n", x1, x2, output);
    }

    getch();
}