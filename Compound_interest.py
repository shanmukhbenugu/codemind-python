import math
p,r,t=map(int,input().split())
a=math.pow((1+(r/100)),t)
print("%.2f"%(p*a))