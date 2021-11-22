import random as r

def res(a,b,c):
	#print('processing res({},{},{},{})'.format(a,b,c,d))
	# terminate
	if b == 1:
		return a
	# number processing
	temp = res(a,b//2,c)
	a = (a ** 2) % c
	b = b // 2
	return a
	
a,b,c = list(map(int,input().split()))
print(res(a,b,c))
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