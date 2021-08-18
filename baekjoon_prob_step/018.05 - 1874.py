n = int(input())
st = [x for x in range(n + 1, 0, -1)]
workst = []
result = []
arr = []
impossible = False
for i in range(0, n):
	arr.append(int(input()))

# init
workst.append(0)
for i in range(0, arr[0]):
	result.append('+')
	workst.append(st[-1])
	st.pop()

# main logic
for i in range(0, n):
	if arr[i] < workst[-1]:
		while arr[i] != workst[-1]:
			result.append('-')
			workst.pop()
	elif arr[i] > workst[-1]:
		if st[-1] > arr[i]:
			print('NO')
			impossible = True
			break
		while arr[i] != workst[-1]:
			result.append('+')
			workst.append(st[-1])
			st.pop()
	result.append('-')
	workst.pop()

if impossible == False:
	for i in result:
		print(i)