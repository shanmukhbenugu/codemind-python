def che(p):
    n=p
    while(p>0):
        r=p%10
        if(r==0):
            return(0)
        elif(n%r!=0):
            return(0)
        p=p//10
    else:
        return(1)
    
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(che(i)):
        print(i,end=" ")