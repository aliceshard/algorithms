def bico(n,k):
	a,b=1,1
	
	if n==0 or k==0:
		return 1
	elif k < 0 or n <k:
		return 0
	
	for i in range(0,k):
		a*=(n-i)
	for i in range(0,k):
		b*=(k-i)
	return int(a/b)

def sol():
	num= int(input())
	arr =[]
	for i in range(0,num):
		arr.append(tuple(map(int,input().split())))
		print(bico(arr[i][1], arr[i][0]))

	
if __name__=='__main__':
	sol()