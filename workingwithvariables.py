#what is variable?
#How to declar variable and User?
#Displaying a variable value using print
#Re-declare variable?
#Delete a variable?
#Rules to define a variable?

'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:  	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:  	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

'''

#Example:1
x=2
y=3*x+4
print(y)
#Exmaple:2
x=5
y="Jhon"
print(type(x))
print(type(y))
#Casting: If you want to specify the data type of a variable, this can be done with casting.
x=str(5)
y=int(3)
z=float(3)
print(x, type(x))
print(y, type(y))
print(z, type(z))

my_value=True
my_new_value=False

print(my_value,type(my_value))
print(my_new_value,type(my_new_value))
