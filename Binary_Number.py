a=int(input())
for i in range(0,(2**(a))):
   b=(bin(i)[2::])
   c=abs(len(b)-a)
   print(c*"0" + b)