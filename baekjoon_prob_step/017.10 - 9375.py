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
		dic.clear()
		# input reception
		m = int(input())
		for j in range(0,m):
			x, y = list(input().split())
			if y in dic:
				dic[y].append(x)
			else:
				dic[y] = [x]
		#print(dic)
		# bino section
		tally=1
		for k in dic.keys():
			tally *= len(dic[k]) + 1
		print(tally - 1)
	

if __name__ == '__main__':
	sol()