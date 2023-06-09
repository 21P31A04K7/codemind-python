n=int(input())
l=list(map(int,input().split()))
c=0
tot=0
for i in range(n):
    m=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            m+=1
    if m==2:
        tot+=l[i]
        c+=1
avg=tot/c
print("%.2f"%avg)