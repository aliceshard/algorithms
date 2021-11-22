def facto(n):
	global mod
	res = 1
	for i in range(1,n+1):
		res *= i
		res %= mod
	return res

def power(a,b):
	global mod
	if b == 1:
		return a
	temp = power(a,b//2)
	
	if b % 2 == 0:
		return (temp ** 2) % mod
	else:
		return  (temp ** 2 * a) % mod

def ferma(n, k):
	global mod
	a = facto(n)
	b = facto(k) * facto(n-k)
	print([a,b])
	bf = power(b, mod-2)
	return (a * bf) % mod
	
mod = 1000000007
n,k = list(map(int,input().split()))
print(ferma(n, k))

