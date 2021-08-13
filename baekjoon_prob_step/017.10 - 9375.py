def bino(n, k):
	a, b = 1, 1
	for i in range(0, k):
		a *= n-i
	for i in range(0,k):
		b *= k-i
	return int(a/b)
		
def sol():
	dic = {}
	n = int(input())
	for i in range(0,n):
		m = int(input())
		for j in range(0,m):
			x, y = list(input().split())
			if y in dic:
				dic[y].append(x)
			else:
				dic[y] = [x]
		tally=1
		for j in range(0)
		print(tally)
	

if __name__ == '__main__':
	sol()