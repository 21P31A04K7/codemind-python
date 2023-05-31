n=int(input())
l=list(map(str,input().split()))
a=[]
for i in l:
    a.append(len(i))
print(a.count(min(a)))