r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1:
            s+=mat[i][j]
        elif j==0 or j==r-1:
            s+=mat[i][j]
print(s)