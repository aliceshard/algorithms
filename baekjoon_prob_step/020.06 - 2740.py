size1 = list(map(int, input().split()))
vec1=[]
for i in range(0, size1[0]):
	temp = list(map(int, input().split()))
	vec1.append(temp)

#print('getting vector2...')
size2 = list(map(int, input().split()))
vec2=[]
for i in range(0, size2[0]):
	temp = list(map(int, input().split()))
	vec2.append(temp)

#print('calculating...')
result = []
for i in range(0, size1[0]):
	temp = []
	for j in range(0, size2[1]):
		acc = 0
		for k in range(0, size1[1]):
			acc += vec1[i][k] * vec2[k][j]
		temp.append(acc)
	result.append(temp)

for i in range(0, size1[0]):
	for j in range(0, size2[1]):
		print('{}'.format(result[i][j]), end=' ')
	print('')