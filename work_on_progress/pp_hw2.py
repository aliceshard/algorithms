atm = dict()
balance = 1000000

while True:
	com = int(input('1) withdraw 2) deposit 3) view log 4) exit'))
	if com == 2:
		name = input('type your name: ')
		money = int(input('how much: '))
		atm[name] = money
		continue
	if com == 1:
		name = input('type your name: ')
		print('we have {} won.', balance)
		money = int(input('how much? '))
		balance -= money
		atm[name] = money * -1
		continue
	if com == 4:
		print('atm end')
		break
	if com == 3:
		print(len(atm))
		for key in atm:
			print('name: {}, money: {}'.format(key, atm[key]))
		continue