l=list(map(str,input().split()))
ll=len(l)
a=[]
for i in range(ll):
    mi=ord(min(l[i]))
    ma=ord(max(l[i]))
    a.append(ma-mi)
print(*a)