l=list(map(str,input().split()))
a=[]
a.append(min(l[0]))
a.append(max(l[len(l)-1]))
print(*a)