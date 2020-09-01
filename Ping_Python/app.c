#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int howMany = 0, i = 0;
    float num1, num2;
    char sign;

    FILE *fp;
    if((fp=fopen("operations.txt", "w"))==NULL)
    {
        exit(-1);
    }

    printf("How many math operations would you like to pass?\n> ");
    scanf("%d", &howMany);

    for(i=0; i<howMany; i++)
    {
        printf("Pass %d operations like this: {num1 sign num2}:\n> ", i+1);
        scanf("%f %c %f", &num1, &sign, &num2);

        fprintf(fp, "%f ", num1);
        fprintf(fp, "%c ", sign);
        fprintf(fp, "%f", num2);
        if(i < howMany-1)
            fprintf(fp, "\n");
    }

    fclose(fp);
    return 0;
}
