
v=10
l=[]
for i in range(v):
    if(i==0):
        l.append(0)
    elif(i==1):
        l.append(1)
    else:
        l.append(l[i-1]+l[i-2])
print(l)

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    fib(n-1)
    
