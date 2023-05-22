s=input()
d={}
for i in s:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
c={}
m=max(d.values())
for k,v in d.items():
    if(v!=m):
        c[k]=v
if(len(c)==0):
    print(-1)
else:
    m=max(c.values())
    for k,v in c.items():
        if(v==m):
            print(k)
            break