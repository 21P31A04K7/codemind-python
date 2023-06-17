s="aeiouAEIOU"
l=list(map(str,input().split()))
max=999
for i in range(len(l)):
    c=0
    for j in l[i]:
        if j in s:
            c+=1
    if c<max:
        max=c
print(max)