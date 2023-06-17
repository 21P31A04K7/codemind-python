l=list(map(str,input().split()))
d=[]
for i in l:
    count=0
    for j in i:
        if j in "aeiouAEIOU":
            count=count+1
    d.append(count)
dup=[]
for i in d:
    if i == min(d):
         dup.append(i)
print(len(dup)) 