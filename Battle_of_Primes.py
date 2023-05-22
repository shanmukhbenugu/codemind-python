def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
        else:
            return(1)
    else:
        return(1)
n1=int(input())
n=n1+int(input())
c=1
while(1):
    if(prime(n+c)):
        print(c)
        break
    else:
        c+=1