from collections import deque

n,k=list(map(int,input().split()))
arr=[x for x in range(1,n+1)]
qu=deque([])

cnt=-1
for i in range(0,n):
	print(arr)
	cnt = (cnt + k) % n
	if(arr[cnt]==-1):
		while arr[cnt]!=-1:
			cnt = (cnt+1)%n
			print(cnt)
	qu.append(arr[cnt])
	arr[cnt]=-1
print(qu)