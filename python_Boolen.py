#Functions can Return a Boolean

class myclass():
    def __len__(self):
        return 0
    def myFunction():
        return True
myobj = myclass()
print(bool(myobj))
#print(bool(myobj.myFunction))
#################################
def myFunction():
    return True
print(myFunction())

if myFunction():
    print("Yes")
    else:
        print("No")