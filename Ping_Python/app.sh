#!/bin/bash
{ 
n=9
echo "$n" 

for (( i=1; $i < 10; i++ )) ; do
       let "c=$i+1" 
       echo $i "+" $c
done
} | ./app
