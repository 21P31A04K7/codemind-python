n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    h=0
    for j in range(n):
        if l[i]==l[j]:
            h+=1
    if h==k:
        print(l[i],end=' ')
        c+=1
        l[i]=0
if c==0:
    print("-1")