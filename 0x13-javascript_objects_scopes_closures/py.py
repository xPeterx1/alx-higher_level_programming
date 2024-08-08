def make_withdraw(balance):
	counter = 1
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return('no fund')
		balance = balance - amount
		nonlocal counter
		counter+=1
		print(counter)
		return balance
	return withdraw
	
wd = make_withdraw(20)
print(wd(5))
print(wd(3))