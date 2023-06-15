n=int(input())
l=list(map(str,input().split()))
a=[];a2=[]
for i in l:
    a.append(len(i))
for i in range(n):
    if a[i]==max(a):
        a2.append(l[i])
print(*a2)