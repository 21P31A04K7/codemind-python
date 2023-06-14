n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
k=n//2
for i in range(k):
    a.append(l[i])
for i in range(k,n):
    b.append(l[i])
print(sum(a))
print(sum(b))