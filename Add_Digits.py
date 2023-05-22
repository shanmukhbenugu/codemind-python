n=input()
if(len(n)==1):
    print(n)
else:
    while(1):
        s=0
        for i in n:
            s+=int(i)
        n=str(s)
        if(len(n)==1):
            break
    print(n)