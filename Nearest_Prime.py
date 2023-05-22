def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
        else:
            return(1)
    else:
        return(0)
for _ in range(int(input())):
    a=int(input())
    if(prime(a)):
        print(a)
    else:
        b=a-1
        c=a+1
        while(1):
            if(prime(b)):
                print(b)
                break
            elif(prime(c)):
                print(c)
                break
            else:
                b-=1
                c+=1