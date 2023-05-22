n=int(input())
a=0
c=0
for i in str(n):
    if(int(i)%2==0):
        c+=1
    else:
        a+=1
if(c==len(str(n))):
    print("Even")
elif(a==len(str(n))):
    print("Odd")
else:
    print("Mixed")