#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    char a[10] = "3.14";
    float fl;
    char stmpbuf[5]="cb";
    sscanf(stmpbuf,"%f",&fl);
    float pi = atof(a);
    printf("Value of pi = %f %fl\n", pi,fl);
    return 0;
}
