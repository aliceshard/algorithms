n=int(input())
st = [x for x in range(n+1,0,-1)]
workst = []
arr=[]
for i in range(0,n):
	arr.append(int(input()))

#init
workst.append(0)
for i in range(0, arr[0]):
	print('+')
	workst.append(st[-1])
	st.pop()
	
#main logic
for i in range(0,n):
	if arr[i] < workst[-1]:
		while arr[i] != workst[-1]:
			print('-')
			workst.pop()
	elif arr[i] > workst[-1]:
		if st[-1] > arr[i]:
			print('impossible')
			break
		while arr[i] != workst[-1]:
			print('+')
			workst.append(st[-1])
			st.pop()
	print('-')
	workst.pop()