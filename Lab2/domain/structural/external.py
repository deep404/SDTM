import time

class Electronic_device:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		time.sleep(1)
		return 'The {} '.format(self.name)

	def play(self):
		time.sleep(1)
		return 'is playing an electronic song!'

class Human:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		time.sleep(1)
		return '{} the customer'.format(self.name)

	def speak(self):
		time.sleep(1)
		return ': Wow it works!'
