n=int(input())
l=list(map(int,input().split()))
a=[]
b=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        print(l[i],end=' ')
        b+=1
        l[i]=0
if b==0:
    print("-1")