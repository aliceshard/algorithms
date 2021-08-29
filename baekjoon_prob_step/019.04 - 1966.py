from collections import deque

c = int(input())
for i in range(0,c):
	n, m = list(map(int,input().split()))
	arr =list(map(int,input().split())) 
	max_pr=max(arr)
	q=deque(arr)
	
	pr_cnt=1
	idx_cnt=0
	while q.empty() != True:
		if q[0] < max_pr:
			q.append(q.popleft())
			idx_cnt += 1
			continue
		