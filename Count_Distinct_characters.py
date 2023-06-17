n=input()
n=n.lower()
a=[]
for i in range(len(n)):
    if n[i]!=' ':
        a.append(n[i])
a=list(set(a))
a.sort()
print(len(a))