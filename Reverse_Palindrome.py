a=input()
b=a[::-1]
c=str(int(a)+int(b))
while(c!=c[::-1]):
    d=int(c)+int(c[::-1])
    c=str(d)
print(c)