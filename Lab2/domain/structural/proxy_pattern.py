
class SensitiveInfo:
	def __init__(self):
		self.users = ['Mihai Moglan']

	def read(self):
		print('There are {} users: {}'.format(len(self.users), ', '.join(self.users)))

	def find(self, user):
		return user in self.users

	def add(self, user):
		self.users.append(user)
		print('Added user {}'. format(user))

class Info:
	'''protection proxy to SensitiveInfo'''

	def __init__(self):
		self.protected = SensitiveInfo()
		self.secret = 'TMPS==design_patterns'

	def read(self):
		self.protected.read()

	def find(self, user):
		if self.protected.find(user):
			print('{} has discount!'.format(user))
			return True
		else:
			print('{} does not have discount!'.format(user))
			return False

	def add(self, user):
		sec = input('What is the secret word? ')
		if sec == self.secret:
			self.protected.add(user)
			return True
		else:
			print("That's wrong!")
			return False

def discount_main(price, discount, customer):
	has_discount = False
	info = Info()
	while True:
		print('1. Check person has discount |==| 2. Add a new person |==| 3. Pay')
		key = input('Choose option: ')

		if key == '2':
			#name = input("What's the name of the fresh person? ")
			has_discount = info.add(customer)
		elif key == '1':
			#name = input("What's the name of the fresh person? ")
			has_discount = info.find(customer)
		elif key == '3':
			break
		else:
			print('Unknown option: {}'.format(key))

	if has_discount:
		print(customer, ', good news, you have', str(discount), "% discount!")
		print(customer, ', you have to pay', str(price * (1 - discount/100)), '!')
	else:
		print(customer, ', unfortunately, you do not have a discount!')
		print(customer, ', you have to pay', str(price), '!')

#if __name__ == '__main__':
#	discount_main('Alex Clefos')