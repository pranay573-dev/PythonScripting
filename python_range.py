'''
range():
-->Range data type represent a sequence of values
-->immutable
'''

#Form-1: range(x)
Number=range(10)
for i in Number:
    print(i)

#Form-2: range(10,30): to represent numbers from 10-29
Number1=range(10,29)
for i in Number1:
    print(i)
#Form-3
Number2=range(10,50,5)
for i in Number2:
    print(i)