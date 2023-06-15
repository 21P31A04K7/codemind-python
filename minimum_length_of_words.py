l=list(map(str,input().split()))
min=999
for i in range(len(l)):
    if len(l[i])<min:
        min=len(l[i])
print(min)