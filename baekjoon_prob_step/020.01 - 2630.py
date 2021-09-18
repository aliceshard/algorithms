white, blue = [0,0]
n=int(input())
arr = []
for i in range(0,n):
	temp = list(map(int,input().split()))
	arr.append(temp)

def recur(row, col, leng):
	if leng==1:
		if arr[row][col]==1:
			blue += 1
			return
		elif arr[row][col]==0:
			white += 1
			return
	# check the chunk whether it's consisted with only 1s
	fit_flag = True
	for i in range(row, row+leng):
		for j in range(col, col+leng):
			if arr[i][j] != 1:
				fit_flag=False
				break
		if fit_flag==False:
			break
	# do recursive job if it's not a fit square
	# issue: add logics checking other chunks that devided
	if fit_flag==False:
		recur(row,col,leng//2)
	elif fit_flag==True:
		blue += 1
		return

