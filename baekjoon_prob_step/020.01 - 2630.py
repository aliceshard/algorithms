white, blue = [0,0]
n=int(input())
arr = []
for i in range(0,n):
	temp = list(map(int,input().split()))
	arr.append(temp)

def recur(row, col, leng):
	if leng==1:
		if arr[row][col]==1:
			return 1
		else:
			return 0
	a = recur(row, col, leng//2)
	b = recur(row+leng//2, col, leng//2)
	c = recur(row+leng//2, col+leng//2, leng//2)
	d = recur(row,col+leng//2,leng//2)
	if a+b+c+d == leng**2:
		return 1
	else:
		blue += a+b+c+d
		white += 4-(a+b+c+d)
		return 0

# main starts from here
res = recur(0,0,n)
if res==1:
	white = 0
	blue = 1
print(blue)
print(white)
