s=input()
ma=0
for i in range(len(s)):
    if(s[i] in "AEIOUaeiuo"):
        c=1
        for j in range(i+1,len(s)):
            if(s[j] not in "AEIUOaeuio"):
                break
            else:
                c+=1
        if(ma<c):
            ma=c
print(ma)