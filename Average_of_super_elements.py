n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    h=0
    for j in range(n):
        if l[i]==l[j]:
            h+=1
    if h==l[i]:
        s+=l[i]
        c+=1
        l[i]=0
if c==0:
    print("-1")
else:
    avg=s/c
    print("%.2f"%avg)
        
        
