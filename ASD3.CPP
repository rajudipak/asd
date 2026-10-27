#include <stdio.h>
#include <conio.h>

void main()
{
    int inputs[4][2] = {
        {0, 0},
        {0, 1},
        {1, 0},
        {1, 1}
    };

    int i, x1, x2, h1, h2, output;

    clrscr();

    printf("XOR Gate using Neural Network\n");

    for (i = 0; i < 4; i++)
    {
        x1 = inputs[i][0];
        x2 = inputs[i][1];

        h1 = (x1 + x2 > 0) ? 1 : 0;
        h2 = (x1 + x2 == 2) ? 1 : 0;

        output = (h1 - h2 > 0) ? 1 : 0;

        printf("%d %d -> %d\n", x1, x2, output);
    }

    getch();
}