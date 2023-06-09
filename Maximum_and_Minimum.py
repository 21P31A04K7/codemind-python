n=int(input())
l=list(map(int,input().split()))
a=[]
min=999
max=0
c=0
for i in range(n):
    h=0
    for j in range(n):
        if l[i]==l[j]:
            h+=1
    if h==l[i]:
        if l[i]<min:
            min=l[i]
        if l[i]>max:
            max=l[i]
        c+=1
        l[i]=0
a.append(min)
a.append(max)
if c==0:
    print("-1")
else:
    print(*a)