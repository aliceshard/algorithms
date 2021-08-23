from collections import deque

n = int(input())
qu = deque([x for x in range(n,0,-1)])


while len(qu) != 1:
	#print(list(qu))
	qu.pop()
	qu.appendleft(qu[-1])
	qu.pop()
print(qu[0])