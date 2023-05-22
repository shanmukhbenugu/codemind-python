n=int(input())
s=n*n
r=0
while(s>0):
    r+=(s%10)
    s=s//10
if(r==n):
    print("Neon Number")
else:
    print("Not Neon Number")