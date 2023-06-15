s='aeiou'
n=input()
a=[]
for i in s:
    c=0
    for j in n:
        if i==j:
            c+=1
    if c==0:
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print('0')