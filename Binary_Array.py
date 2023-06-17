n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]==0:
        c+=1
    elif l[i]==1:
        c+=1
    else:
        c-=1
if c==n:
    print("True")
else:
    print("False")