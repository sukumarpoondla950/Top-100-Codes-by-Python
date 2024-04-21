#Leap year or not
x=int(input("Enter a number:"))
if(x%4==0 and x%100!=0):
    print(x,"is a Leap Year")
elif(x%400==0):
    print(x,"is a Leap Year")
else:
    print(x,"is a not a  Leap Year")
