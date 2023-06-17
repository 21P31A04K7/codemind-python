n=input()
a=[]
b=[]
c=0
d=0
for i in range(len(n)):
    if n[i]!=' ':
        a.append(n[i])
a.sort()
l=len(a)
for i in a:
    if i==a[0]:
        c+=1
for i in a:
    if i==a[l-1]:
        d+=1
    
b.append(a[0])
b.append(c)
b.append(a[len(a)-1])
b.append(d)
print(*b)