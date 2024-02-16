#Greatest of the Three numbers:
x=int(input("Enter 1st number="))
y=int(input("Enter 2nd number="))
z=int(input("Enter 3rd number="))
if(x>y and x>z):
    print(x,"is Greatest of the Three numbers")
elif(y>z and y>x):
    print(y,"is Greatest of the Three numbers")
else:
    print(z,"is Greatest of the Three numbers")

