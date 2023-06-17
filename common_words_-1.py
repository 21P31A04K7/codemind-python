l=list(map(str,input().split()))
ll=[]
ll1=[]
s=[]
for i in l:
    ll.append(i.lower())
l1=list(map(str,input().split()))
for i in l1:
    ll1.append(i.lower())
for i in ll:
    if i in ll1:
        s.append(i)
print(len(s))