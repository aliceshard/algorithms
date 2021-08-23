from collections import deque

n,k=list(map(int,input().split()))
arr=[x for x in range(1,n+1)]
qu=deque([])

cnt=0
for i in range(0,n):
    #print(arr)
    while arr[cnt] == -1:
        cnt = (cnt + 1) % n

    for j in range(0, k-1):
        while arr[cnt] == -1:
            cnt = (cnt + 1) % n
        cnt = (cnt + 1) % n

    while arr[cnt] == -1:
        cnt = (cnt + 1) % n
    qu.append(arr[cnt])
    arr[cnt] = -1

print('<', end='')
print(qu[0], end='')
for i in range(1,n):
    print(', ', end='')
    print(qu[i], end='')
print('>', end='')