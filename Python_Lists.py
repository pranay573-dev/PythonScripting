'''
#################################Python Collections (Arrays)###############################################
There are four collection data types in the Python programming language:

bytes and bytearray: bytes are immutable(Unchangable) and bytearray is mutable(changable):::::[]
List is a collection which is ordered and changeable. Allows duplicate members.::::[]
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.:::::()
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.

'''

# Lists are used to store mutliple items in a single variable. 
# Lists are one of 4 built-in data types in python used to store collections of data, the other 3 are
        # Tuple
        # Set
        # Dictonary


# Lists are created using square brackets
#List items are ordered, changeable, and allow duplicate values. 
# A List can contain different data types
# Lists are growable in nature

# Example 1: List Iteams

list1=["apple","bananna","Cherry"]
print(len(list1))

#Example 2: Allow Dubplicates
list2=["Graps","Orange", "Graps", "Orange" ]
print(list2)


# Find the data type of List
list3 = ["apple", "banana", "cherry"]
list4 = [1, 5, 7, 9, 3]
list5 = [True, False, False]
print(type(list3), type(list4), type(list5))

#A list can contain different data types:
list6=["abc",34,True,40,"Male"]
print(list6)
