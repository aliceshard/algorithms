import sys

qu=[]
tail,rear=0,0
n=int(input())

for i in range(0,n):
	temp=list(sys.stdin.readline().split())
	if temp[0] == 'push':
		qu.append(temp[1])
		rear +=1
		continue
	elif temp[0] == 'pop':
		if rear == tail:
			print(-1)
			continue
		print(qu[tail])
		tail +=1
	elif temp[0] == 'size':
		print(rear-tail)
	elif temp[0] == 'empty':
		if rear==tail:
			print(1)
		else:
			print(0)
	elif temp[0] == 'front':
		if rear==tail:
			print(-1)
			continue
		print(int(qu[rear-1]))
	elif temp[0] == 'back':
		if rear==tail:
			print(-1)
			continue
		print(int(qu[tail]))