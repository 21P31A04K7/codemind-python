s=input()
s=s.split()
y=0
for i in range(len(s)-1,-1,-1):
    x=s[i]
    y=min(x)
    if y.lower() in x:
        print(y.lower())
    else:
        print(y)
    break