Number1=eval(input("Please enter your first number:"))
Number2=eval(input("Please enter your second number:"))
Operation=eval(input("Which operation you want us to perform:"))
Result=0
if Operation == "ADD":
    Result=Number1+Number2
    print(Result)
elif Operation == "SUB":
    Result= Number1-Number2
    print(Result)
elif Operation == "DIV":
    Result= Number1%Number2
    print(Result)