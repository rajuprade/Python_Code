#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    unsigned char s[5] ={ 0xcb,0x82,0xc9,0xff,0xdd};
    float f;
    long l;
    unsigned char tmp[10];
    unsigned char *t = NULL;
    t = (unsigned char*)malloc(sizeof(unsigned char )*512); 
    
/*    strcpy(tmp,s);
    l = strtol(tmp, (char**)NULL, 16);
    f = (float)l; */

     printf("##############%f\n",f); 
      sprintf(t,"%x",s[2]);
     printf("##############%s %x\n",t,s[2]); 
     
      l = strtol(t,NULL, 16);
      f = (float)l;

     printf("After Sprintf ##############%f\n", f);
 
}
