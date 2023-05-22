n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    s=l[i]
    a.append(s)
    for j in range(i+1,n):
        s+=l[j]
        a.append(s)
print(max(a))