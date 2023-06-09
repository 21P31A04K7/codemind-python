n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
mi=0
c=0
for i in range(n):
    if l[i]>=a and l[i]<=b:
        if l[i]>mi:
            mi=l[i]
            c+=1
if c==0:
    print("-1")
else:
    print(mi)