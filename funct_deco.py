# A Python example to demonstrate that 
# decorators can be useful attach data 

# A decorator function to attach 
# data to func 
def attach_data(func): 
	func.data = 3
	return func 

@attach_data
def add (x, y): 
	return x + y 

# Driver code 

# This call is equivalent to attach_data() 
# with add() as parameter 
print(add(2, 3)) 

print(add.data) 

#add() returns sum of x and y passed as arguments but it is wrapped 
# by a decorator function, calling add(2, 3) would simply give 
#sum of two numbers but when we call add.data then add 
#function is passed into then decorator function atta#ch_data 
#as argument and this function returns add 
#function with an attribute 
#data that is set to 3 and hence prints it.
