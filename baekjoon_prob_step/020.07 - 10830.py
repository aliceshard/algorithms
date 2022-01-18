def vec_mul(vec, n):
	print('calculating...')
	result = []
	for i in range(0, n):
		temp = []
		for j in range(0, n):
			acc = 0
			for k in range(0, n):
				acc += vec[i][k] * vec[k][j]
			temp.append(acc)
		result.append(temp)
	return result

def factor_bin(b):
	temp = []
	while(b != 0):
		if b % 2 == 0:
			b 

#print('getting vector input...')
size = list(map(int, input().split()))
vec=[]
for i in range(0, size2[0]):
	temp = list(map(int, input().split()))
	vec.append(temp)

for i in range(0, size1[0]):
	for j in range(0, size2[1]):
		print('{}'.format(result[i][j]), end=' ')
	print('')