r,m=map(str,input().split())
for i in r:
    if(r.count(i)>m.count(i)):
        print(False)
        break
else:
    print(True)