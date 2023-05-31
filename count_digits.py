n=int(input())

l=list(map(str,input().split()))
a=[]
for i in l:
    le=0
    for char in i:
        if char!='-':
            le+=1
    a.append(le)
print(*a)