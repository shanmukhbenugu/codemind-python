s=list(input().split(" "))
a=1
c=''
for i in s:
    if(i[0] in "AEIOUaeiuo"):
        c+=i+"ma"+(a*"a")+" "
        a+=1
    else:
        c+=i[1::]+i[0]+"ma"+a*"a"+" "
        a+=1
print(c[0:-1])