#Sum of numbers in a given range
x=int(input("Enter a small range:"))
y=int(input("Enter a  big range:"))
s=0
"""while(x<=y):
    s=x+s
    x=x+1
    print("s:",s)
print("Sum of numbers in a given range:",s)"""
for i in range(x,y+1):
    s=s+i
print("Sum of numbers in a given range:",s)
    
