#Sum of First N Natural numbers
x=int(input("Enter a number:"))
s=0
for i in range(1,x+1,1):
    s=s+i
print("Sum of First N Natural numbers=",s)
