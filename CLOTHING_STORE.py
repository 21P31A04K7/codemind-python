n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
d=0
for i in b:
   c=a.count(i)
   d+=c//2
print(d)