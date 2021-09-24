a,b,c = list(map(int,input().split()))
acc = a
for i in range(0,b):
	acc *= a
	acc = acc%c
print(acc)