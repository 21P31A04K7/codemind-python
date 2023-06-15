a=input()
a=a.lower()
b=input()
b=b.lower()
s=[]
for i in a:
    if i in  b:
        if i not in s:
            if i!=' ':
                s.append(i)
for i in b:
    if i in a:
        if i not in s:
            if i!=' ':
                s.append(i)
s=sorted(s)
print(len(s))