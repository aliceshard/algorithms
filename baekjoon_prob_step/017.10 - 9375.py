def sol():
	n,k = list(map(int,input().split()))
	memo = {}
	memo[0] = [1,0]
	for i in range(0,n+1):
		memo[i] = [1]
		for j in range(1, n+2):
			memo[i].append(0)

	for i in range(1, n+1):
		for j in range(1, i+2):
			memo[i][j] = (memo[i-1][j-1] + memo[i-1][j]) % 10007

	print(memo[n][k])


if __name__ == '__main__':
	sol()