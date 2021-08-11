arr = []
while True:
	temp = tuple(map(int, input().split()))
	if temp[0] == 0 and temp[1] == 0:
		break
	arr.append(temp)
n=len(arr)

for i in range(0, n):
	cursor = arr[i]
	if cursor[0] % cursor[1] ==0:
		print('multiple')
	elif cursor[1] % cursor[0]==0:
		print('factor')
	else:
		print('neither')
