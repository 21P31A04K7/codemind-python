n=int(input())
arr=list(map(int,input().split()))
if arr[0]<arr[1]:
    s=0
    for i in range(n-1):
        if i%2==0:
            if arr[i]>=arr[i+1]:
                s=1
    if s==0:
        print('yes')
    else:
        print('no')
else:
    s=0
    for i in range(1,n):
        if i%2!=0:
            if arr[i]>arr[i-1]:
                s=1
    if s==0:
        print('yes')
    else:
        print('no')