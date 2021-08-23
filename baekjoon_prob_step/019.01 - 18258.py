import sys

qu=[]
tail, front= 0, 0
n=int(input())

for i in range(0,n):
	temp= list(sys.stdin.readline().split())

	if temp[0] == 'push':
		qu.append(temp[1])
		front += 1

	elif temp[0] == 'pop':
		if front == tail:
			print(-1)
			continue
		print(qu[tail])
		tail += 1

	elif temp[0] == 'size':
		print(front - tail)

	elif temp[0] == 'empty':
		if front == tail:
			print(1)
		else:
			print(0)

	elif temp[0] == 'back':
		if front==tail:
			print(-1)
			continue
		print(qu[front - 1])

	elif temp[0] == 'front':
		if front==tail:
			print(-1)
			continue
		print(qu[tail])