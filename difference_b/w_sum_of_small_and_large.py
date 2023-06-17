l=list(map(str,input().split()))
ll=len(l)
s=0
s1=0
for i in range(ll):
    s=s+ord(min(l[i]))
    s1=s1+ord(max(l[i]))
print(s1-s)