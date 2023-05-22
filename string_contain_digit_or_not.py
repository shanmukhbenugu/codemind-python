s=input()
d=0
for i in s:
    if(i.isdigit()):
        d+=1
if(d==0):
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%d)