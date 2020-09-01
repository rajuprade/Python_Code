#!/usr/bin/python 
def changeme( mylist ): 
	mylist.append([1,2,3,4]);
	print "Values inside the function: ", mylist
	return
# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

# Function definition is here
def printinfo( name, age ):
	"This prints a passed info into this function"
	print "Name: ", name;
	print "Age ", age;
	return;
# Now you can call printinfo function
printinfo( age=33, name="RAJU" );

def sum( arg1, arg2 ):
# Add both the parameters and return them."
	total = arg1 + arg2
	print "Inside the function : ", total
	return total;
# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total

