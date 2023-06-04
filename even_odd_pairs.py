n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)>len(o):
    for i in range(len(e)-len(o)):
        o.append(0)
else:
    for i in range(len(o)-len(e)):
        e.append(0)
f=[]
ff=[]
for i in range(len(e)):
    f.append(e[i])
    f.append(o[i])
for i in f:
    if i!=0:
        ff.append(i)
if len(ff)%2==1:
    ff.append(0)
print(*ff)