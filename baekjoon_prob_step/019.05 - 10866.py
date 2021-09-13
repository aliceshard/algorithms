from collections import deque
from sys import stdin

n = int(input())
q = deque([])
for i in range(0,n):
	temp = stdin.readline().split()
	if temp[0]=='push_front':
		q.appendleft(int(temp[1]))
		continue
	elif temp[0]=='push_back':
		q.append(int(temp[1]))
		continue
	elif temp[0]=='pop_front':
		if len(q)==0:
			print(-1)
		else:
			print(q.popleft())
		continue
	elif temp[0]=='pop_back':
		if len(q)==0:
			print(-1)
		else:
			print(q.pop())
		continue
	elif temp[0]=='size':
		print(len(q))
		continue
	elif temp[0]=='empty':
		if len(q)==0:
			print(1)
		else:
			print(0)
		continue
	elif temp[0]=='front':
		if len(q)==0:
			print(-1)
		else:
			print(q[0])
		continue
	elif temp[0]=='back':
		if len(q)==0:
			print(-1)
		else:
			print(q[-1])
		continue