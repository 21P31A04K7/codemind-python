l=list(map(str,input().split()))
ll=[]
ll1=[]
for i in l:
    ll.append(i.lower())
l1=list(map(str,input().split()))
for i in l1:
    ll1.append(i.lower())
s=[]

for i in ll1:
    if i in ll:
        if i not in s:
            s.append(i)
print(*s)