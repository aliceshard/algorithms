from collections import deque

n,k=list(map(int,input().split()))
arr=[x for x in range(1,n+1)]
qu=deque([])

cnt=0
for i in range(0,n):
	cnt = (cnt + (k-1)) % (n-i)
	arr.