def GCD(a, b):
	if a<b:
		a,b = b,a
	while a%b!=0:
		temp = b
		b = a%b
		a = temp
	return b
	

n=int(input())
arr=list(map(int,input().split()))
	
for i in range(1,n):
	gcd=GCD(arr[0], arr[i])
	print(str(int(arr[0]/gcd)) + '/' + str(int(arr[i]/gcd)))
	