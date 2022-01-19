def vec_mul(vec1, vec2, n):
	#print('calculating...')
	result = []
	md = 1000
	for i in range(0, n):
		temp = []
		for j in range(0, n):
			acc = 0
			for k in range(0, n):
				acc += (vec1[i][k] * vec2[k][j])%md
			acc %= md
			temp.append(acc)
		result.append(temp)
	return result

def factor_bin(b):
	temp = []
	while(b != 0):
		if b % 2 == 0:
			temp.append(0)
			b //= 2
		elif b % 2 == 1:
			temp.append(1)
			b //= 2
	#print('factored bin: {}'.format(temp))
	return temp

def init_idv(n):
	idv = []
	for i in range(0,n):
		temp = []
		for j in range(0,n):
			if i == j:
				temp.append(1)
			else:
				temp.append(0)
		idv.append(temp)
	return idv

def vec_proc(vec, n, b):
	bin_str = factor_bin(b)
	acc_vec = vec
	res_vec = init_idv(n)
	for i in range(0, len(bin_str)):
		if bin_str[i] == 1:
			#print('bit is one...')
			res_vec = vec_mul(res_vec, acc_vec,n)
		acc_vec = vec_mul(acc_vec, acc_vec, n)
		#print(acc_vec)
	return res_vec
	
#print('getting vector input...')
n, b = list(map(int, input().split()))
vec=[]
result = []
for i in range(0, n):
	temp = list(map(int, input().split()))
	vec.append(temp)

result = vec_proc(vec, n, b)

# print
for i in range(0, n):
	for j in range(0, n):
		print('{}'.format(result[i][j]), end=' ')
	print('')