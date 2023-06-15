n=input()
m=input()
h=0
for i in range(len(n)):
    if n[i]==m[0]:
        c=i
        h+=1
        break
if h>0:
    print("True")
    print(c)
else:
    print("False")