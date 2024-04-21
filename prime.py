#prime
x=int(input("Enter a number:"))
c=0
for i in range(1,x+1,1):
    if(x%i==0):
        c=c+1
if (c==2):
    print(x,"is prime number")
else:
    print(x,"Not a prime number")
