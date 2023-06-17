s="aeiouAEIOU"
l=list(map(str,input().split()))
a=[]
for i in range(len(l)):
    c=0
    for j in l[i]:
        if j in s:
            c+=1
    a.append(c)
print(*a)