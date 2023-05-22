s=input()
l=list(s)
a=''
for i in l:
    if(i in "AEIOUaeiou"):
        a+=i
l=l[::-1]
c=0
for i in range(len(l)):
    if l[i] in "AEIOUaeiou":
        l[i]=a[c]
        c+=1
for j in l[::-1]:
    print(j,end="")