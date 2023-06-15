l=list(map(str,input().split()))
s="aeiouAEIOU"
c=0
for i in l:
    if i[0] in s:
        c+=1
print(c)