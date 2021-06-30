'''
What is String in Python:
    A String is a sequence of characters.
How to create a String:
    String_1="Pranaysagar Reddy"
'''
'''
#1
print ('My First Name is: Pranay')
# Assign String to a Variable
a='Hello'
print(a)
#Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
        #Print all above print values in single print
print(f"\n{a},\n{b}")

##################################################Strings are Arrays######################################################
first_name='Pranasyagar Reddy'
print(first_name[1])
#for i in first_name:
#   print(i[0])
#exit
##################################################Check String###################################################
txt="The best things in life are free!"
print("free" in txt)
#Use it in an if statement: (Using IN Keyword)
if "string" in txt:
    print("Free word is available in the sting")
else:
    print("The search string is not available")
#Use it in an if statement: (Using NOT IN Keyword)
if "Free" not in txt:
    print("The search string is not available in the text")
else:
    print("The search string is avaialbe in the text")


#######################################################SLICING###################################################
Name="Pranaysagar Reddy Kadapanavenkata"
print(Name[0:5])
print(Name[:5]) #Slice From the Start
print(Name[2:]) #Get the characters from position 2, and all the way to the end:

##Negative Indexing
Text="World!"
print(Text[-5:-2])
'''
####################################################Python - Modify Strings########################################
a=" Hello, World!  "
c="Pranaysagar Reddy Kadapanavenakta"
b=print(a.upper())# Turn the string into upper case
print(a.casefold())# Trunt the string into lower case
print(a.strip()) # Remove front and end spaces from the string
print(a.replace("Hello", "Hi"))#The replace() method replaces a string with another string:
split1=print(c.split())#The split() method returns a list where the text between the specified separator becomes the list items.
for i in split1:
    print(i[0])
    