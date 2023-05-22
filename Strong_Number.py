num = int(input())  
sum = 0  
temp = num  
while(temp > 0):  
    fact = 1  
    rem = temp % 10  
  
    for i in range(1, rem + 1):  
        fact = fact * i  
    sum = sum + fact  
    temp = temp // 10  
if (sum == num):  
    print("The number %d is a strong number"%num)  
else:  
    print("The number %d is not a strong number"%num) 