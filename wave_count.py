n=int(input())
l=list(map(int,input().split()))
i=c=s=0
while(i+2<=n-1):
    if l[i]>=l[i+1] or l[i+1]<=l[i+2]:
        c+=1
    if l[i]<l[i+1] and l[i+1]>l[i+2]:
        s+=1
    i+=2
if c>0:
    print(-1)
else:
    print(s)
