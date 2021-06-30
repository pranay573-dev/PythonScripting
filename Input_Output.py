#Input and Output syntax
'''
    Keywords:
        --> INPUT
        --> eval: This is convert the datatype automatically according to the assigned value
'''

#First_Name= input("Please Enter your First Name:")
#Second_Name=input("Your Second Name is:")
#Company_Name=input("Your Compnay Name is:")
#ID=input("Please enter your ID:")
#print(f"\nYour First Name is: {First_Name},\nYour Second Name is: {Second_Name},\n Your Compnay Name is:{Company_Name} ")

# Eval Function
First_Name= eval(input("Please Enter your First Name:"))
ID=eval(input("Please enter your ID:"))

print(type(First_Name),type(ID))
