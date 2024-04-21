a=int((input()))
b=int(input())
if(a>b):
    t=a
    a=b
    b=t
for i in range(a,b+1):
    if(i!=1):
        c=True
        for j in range(2,i):
            if(i%j==0):
                c=False
                break
        if(c):
            print(i)
