n=input()
n=n.lower()
a=[]
for i in range(len(n)):
    if n[i]!=' ':
        a.append(n[i])
a=list(set(a))
a.sort()
for i in range(len(a)):
    print(a[i],end='')