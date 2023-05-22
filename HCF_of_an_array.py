n=int(input())
l=list(map(int,input().split()))
c=[]
b=[]
for i in range(len(l)):
    a=l[i]
    for j in range(1,min(l)+1):
        if(a%j==0):
            c.append(j)
for i in range(len(c)):
    if(c[i] not in b)and(c.count(c[i])==len(l)):
        b.append(c[i])
print(max(b))