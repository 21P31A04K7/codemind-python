r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
lst=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    lst.append(s)
print(*lst)