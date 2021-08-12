n,k= list(map(int,input().split()))
a,b=1,1
for i in range(0,k):
	a*=(n-i)
for i in range(0,k):
	b*=(k-i)

if n==0 or k==0:
	print(1)
elif k < 0 or n <k:
	print(0)
else:
	print(int(a/b))