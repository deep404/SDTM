from domain.structural.external import Electronic_device, Human
import time

class Computer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		time.sleep(1)
		return 'The {}'.format(self.name)

	def execute(self):
		time.sleep(1)
		return 'executes a program'

class Adapter:
	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)

def check_electronics_main(type_electronics, customer):
	objects = [Computer(type_electronics)]
	device = Electronic_device(type_electronics)
	objects.append(Adapter(device, dict(execute=device.play)))
	human = Human(customer)
	objects.append(Adapter(human, dict(execute = human.speak)))

	for i in objects:
		print('{} {}'.format(str(i), i.execute()))

#if __name__ == '__main__':
#	check_electronics_main('ASUS', 'Ion')