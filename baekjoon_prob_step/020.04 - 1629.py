import random as r

def res(a,b,c,d):
	#print('processing res({},{},{},{})'.format(a,b,c,d))
	# terminate
	if b == 1:
		if d != 0:
			return (a*d)%c
		else:
			return a % c
	# number processing
	if b % 2 == 1:
		if d == 0:
			d = a
		else:
			d = (a*d)%c
	a = (a ** 2) % c
	b = b // 2
	return res(a,b,c,d)

a,b,c = list(map(int,input().split()))
print(res(a,b,c,0))
#print("actual result: {}".format((a**b)%c))

# logic test
'''
while True:
	a,b,c = [r.randint(1, 100) for i in range(0,3)]
	print(a,b,c)
	d = 0
	result = res(a,b,c,d)
	ac_result = (a**b)%c
	
	if result != ac_result:
		print("calculated: {}".format(result))
		print("actual result: {}".format((a**b)%c))
		break
'''