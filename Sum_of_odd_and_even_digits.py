n=int(input())
a=list(map(int,input().split()))
sum=0
s=0
for i in range(n):
    if(i%2==0):
        sum=sum+a[i]
    else:
        s=s+a[i]
if(sum-s==0):
    print("YES")
else:
    print("NO")