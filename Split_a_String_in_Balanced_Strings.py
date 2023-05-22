d={"L":-1,"R":1}
n=input()
s=0
c=0
for i in n:
    s+=d[i]
    if(s==0):
        c+=1
print(c)