n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n):
    c=0
    while(l[i]!=0):
        r=l[i]%10
        c+=1
        l[i]=l[i]//10
    if c%2==0:
        f+=1
print(f)