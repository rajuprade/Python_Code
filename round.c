#include <stdio.h>
#include <math.h>
int main(void)
{
 double a; 
 for(a=12;a<13;a+=0.1)
    printf("round of  %.1lf is  %.1lf\n", a, round(a));
  return 0;
}
