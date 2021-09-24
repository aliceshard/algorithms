from sys import stdin
n=int(input())
arr=[]
str='('
for i in range(0,n):
	arr.append(stdin.readline().rstrip())

def recur(x,y,leng):
	acc = 0
	bstr = '('
	
	# if length of cell is 1
	if leng == 1:
		if arr[x,y] == 0:
			return 0
		else:
			return 1
	
	#traverse all cells in arr
	for i in range(y, y+leng//2):
		for j in range(x, x+leng//2):
			acc += int(arr[i,j])
	
	#decision logic
	if acc == 2**(leng):
		return '(1)'
	elif acc == 0:
		return '(0)'
	else:
		a = recur(x, y, leng//2)
		b = recur(x+leng//2,y,leng//2)
		c = recur(x,y+leng//2,leng//2)
		d = recur(x+leng//2,y+leng//2,leng//2)
		for i in [a,b,c,d]:
			if len(i) == 3:
				i = i[1]
		bstr += str(a) + str(b) + str(c) + str(d) + ')'
		return bstr

res = recur(0,0,n)
