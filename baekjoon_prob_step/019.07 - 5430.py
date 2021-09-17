from collections import deque
t=int(input())

for i in range(0,t):
	p=input()
	n=int(input())
	arr=input()
	if arr=='[]':
		arr = []
	else:
		arr=deque(list(map(int,arr[1:-1].split(','))))
	err_flag = False
	r_flag = False
	
	for j in range(0,len(p)):
		if p[j] == 'R':
			r_flag = not r_flag
			continue
		elif p[j]=='D':
			if len(arr)==0: 
				err_flag = True
				break
			if r_flag == False:
				arr.popleft()
			else:
				arr.pop()
			continue
	
	if err_flag == True:
		print('error')
	elif err_flag==False:
		if r_flag == False:
			print(str(list(arr)).replace(' ',''))
		elif r_flag==True:
			print(str(list(arr)[::-1]).replace(' ',''))