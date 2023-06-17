n=input()
n=n.lower()
s=0
for i in n:
    c=0
    for j in range(len(n)):
        if i==n[j]:
            c+=1
    if c==1:
        print(i)
        s+=1
        break
if s==0:
    print("-1")