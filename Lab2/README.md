# Creational Design Patterns Laboratory Work No2
## Author: Moglan Mihai, FAF - 192
------
## Introduction
__1. The topic behind this laboratory work is 'Management of electronics store', where the customer selects what type of electronic device he wants and for some gadgets he even selects the parameters for different parts.__

__2. After the selection of electronic device, the customer selects if he/she wants to check the device, what cover he/she wants and the last step is paying for the gadget with oportunity to have a discount.__

__3. The design patterns used in this laboratory work are:__
  * Factory Method
  * Abstract Factory
  * Builder
  * Proxy
  * Decorator
  * Adapter

## Implementation & Explanation
In order to simulate the building of an electronic device is was used the function ```time.sleep()```.

__1. The new computer analogy help to distinguish between a Builder pattern and a Factory pattern. If the customer decides to buy a specific preconfigured computer model, for example, the latest Apple 3.2 GHz Mac Air, it is used the Factory pattern. All the hardware specification are already predefined by the manufacturer, who knows what to do without consulting the customer. The manufacturer typically receives just a single instruction. Code-wise, this would look like the following (`factory_method.py`):__
```python
import time

Air13 = '3.2GHz Mac Air'

class AppleFactory:
	class MacAir13:
		def __init__(self):
			self.memory = 16 # in gigabytes
			self.ssd = 256 # in gigabytes
			self.gpu = 'Apple M1 8-core chip'
		
		def __str__(self):
			print('inserting RAM ...')
			time.sleep(1)
			print('putting SSD ...')
			time.sleep(1)
			print('installing the GPU ...')
			time.sleep(1)
			print('preparing last details ...')
			time.sleep(3)
			print('your Mac Air is ready!', end = '\n\n')
			
			info = ('Model: {}'.format(Air13),
					'Memory: {}Gb'.format(self.memory),
					'SSD: {}Gb'.format(self.ssd),
					'Graphics Card: {}'.format(self.gpu))
			return '\n'.join(info)
		
	def build_computer(self, model):
		if(model == Air13):
			return self.MacAir13()
		else:
			print('We can not build {}'.format(model))

def mac_main():
	afac = AppleFactory()
	mac_air = afac.build_computer(Air13)
	print(mac_air, end = '\n\n')
```

__2. Anoter option is buying a custop Desktop. In this case, is used the Builder pattern. The director gives orders to the manufacturer (builder) about the ideal computer specifications that were given by the customer. Code-wise, this looks like the following (`builder.py`):__
```python
import time

class Desktop:
	def __init__(self, serial_number):
		self.serial = serial_number
		self.memory = None # in gigabytes
		self.ssd = None # in gigabytes
		self.gpu = None # in gigabytes

	def __str__(self):
		info = ('Memory: {}Gb'.format(self.memory),
				'SSD: {}Gb'.format(self.ssd),
				'Graphics Card: {}'.format(self.gpu))
		return '\n'.join(info)

class DesktopBuilder:
	def __init__(self):
		pass

	def configure_memory(self, amount):
		print('inserting RAM ...')
		time.sleep(1)		
		self.desktop.memory = amount

	def configure_ssd(self, amount):
		print('putting SSD ...')
		time.sleep(1)
		self.desktop.ssd = amount

	def configure_gpu(self, gpu_model):
		print('installing the GPU ...')
		time.sleep(1)		
		self.desktop.gpu = gpu_model


class HardwareEngineer:
	def __init__(self):
		self.builder = None

	def construct_computer(self, memory, ssd, gpu):
		self.builder = DesktopBuilder()
		[step for step in (self.builder.configure_memory(memory),
						   self.builder.configure_ssd(ssd),
						   self.builder.configure_gpu(gpu))]
		print('preparing last details ...')
		time.sleep(3)

	@property
	def desktop(self):
		print('your personalized Desktop is ready!', end ='\n\n')		
		return self.builder.desktop
	

def desktop_main():
	ssd = input('What is the size of the SSD (in Gb)?  ')
	ram = input('What is the ram memory (in Gb)? ')
	gpu = input('What is the GPU in your desktop? ')
	print('\n')
	engineer = HardwareEngineer()
	engineer.construct_computer(ssd = ssd, memory = ram, gpu = gpu)
	desktop = engineer.desktop
	print(desktop)

```

The basic changes are the intoduction of a builder `DesktopBuilder`, a director `HardwareEngineer`, and the step-by-step construction of a desktop, which now supportts different configurations (cpu, gpu and ssd)


__3. To Abstract Method was used in the creation of notebook. There are 2 types of notebooks office and gaming one. The main specifications for notebook remains the same: cpu, ssd and gpu. For every type of notebook the specifications classes are different (`abstract_factory`):__
```python
class Gaming_ssd:
	def __init__(self):
		self.parameters = '1024'

	def get_param(self):
		return self.parameters

class Gaming_cpu:
	def __init__(self):
		self.parameters = '16'

	def get_param(self):
		return self.parameters

class Gaming_gpu:
	def __init__(self):
		self.parameters = 'NVidia GeForce RTX 3080 Ti'
	
	def get_param(self):
		return self.parameters

class Office_cpu:
	def __init__(self):
		self.parameters = '8'

	def get_param(self):
		return self.parameters

class Office_ssd:
	def __init__(self):
		self.parameters = '256'

	def get_param(self):
		return self.parameters

class Office_gpu:
	def __init__(self):
		self.parameters = 'Intel HD Graphics'

	def get_param(self):
		return self.parameters 

```

The `GamingNotebook` and `OfficeNotebook` classes are Abstract Factory. Its main responsabilities are creating the notebook with specific characteristics. Keeping the creation methods separate and their names generic (for example `make_cpu()`, `make_gpu()` and `make_ssd()`) allows to dynamically change the active factory without code changes. In a statically typed language, the Abstract Factory would be an abstract class/interface with empty methods, but in Python this is not required because the types are checked in runtime as follows:
```python
class GamingNotebook:
	def __init__(self):
		#print(self)
		self.notebook_type = 'Gaming Notebook'

	def make_cpu(self):
		print('inserting RAM ...')
		time.sleep(1)
		return Gaming_cpu()

	def make_ssd(self):
		print('putting SSD ...')
		time.sleep(1)
		return Gaming_ssd()

	def make_gpu(self):
		print('installing the GPU ...')
		time.sleep(1)
		return Gaming_gpu()



class OfficeNotebook:
	def __init__(self):
		#print(self)
		self.notebook_type = 'Office Notebook'

	def make_cpu(self):
		print('inserting RAM ...')
		time.sleep(1)
		return Office_cpu()

	def make_ssd(self):
		print('putting SSD ...')
		time.sleep(1)
		return Office_ssd()

	def make_gpu(self):
		print('installing the GPU ...')
		time.sleep(1)
		return Office_gpu()
```
The `NotebookEnvironment` is the main entry of the notebook building section. It accepts `factory` as an input, and uses it to create the notebook.

```python
class NotebookEnvironment:
	def __init__(self, factory):
		self.cpu = factory.make_cpu(self)
		self.ssd = factory.make_ssd(self)
		self.gpu = factory.make_gpu(self)

	def __str__(self):
		print('preparing last details ...')
		time.sleep(3)
		print('your personalized Notebook is ready!', end ='\n\n')		
		info = ('Memory: {}Gb'.format(self.cpu.get_param()),
				'SSD: {}Gb'.format(self.ssd.get_param()),
				'Graphics Card: {}'.format(self.gpu.get_param()))
		return '\n'.join(info)
```

The `validate_notebook()` function prompts the user to specifi what type of notebook he wants. There exist 2 types of notebooks: office and gaming one.
```python
def validate_notebook():
	zakaz = True
	while zakaz:
		notebook_type = input('Do you need an [o]ffice or [g]aming notebook? ')
		print('\n')
		if notebook_type != 'o' and notebook_type != 'g':
			print('Sorry, only office (key o) and gaming (key g) notebooks are available', end = '\n')
		else:
			zakaz = False		
	return notebook_type
```

Last but not least comes the `main_notebook()` function.

```python
def main_notebook():
	notebook_type = validate_notebook()
	notebook = OfficeNotebook if notebook_type == 'o' else GamingNotebook
	environment = NotebookEnvironment(notebook)
	print(environment)
```

__4. Before buying the piece of device the customer wants, he/she have the oportunity to check if its working. This can be done via the Adapter design pattern. Our application has a `Computer` class that shows basic information about a computer. All the classes of this example, including the `Computer` class are very primitive, because I want to focus on the Adapter pattern and not on how to make a class as complete as possible (`adapter_pattern.py`):__
```python
class Computer:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		time.sleep(1)
		return 'The {}'.format(self.name)

	def execute(self):
		time.sleep(1)
		return 'executes a program'
```
In this case, the `execute()` method is the main action that the computer can perform. This method is called by the client code. I decided to enrich the app with more functionality, and luckily, I find two interesting classes implemented in two different libraries that are unrelated with out application: `Electronic_device` and `Human`. In the `Electronic_device` clas, the main action is performed by the `play()` method. In the `Human` class, it is performed by the `speak()` method. To indicate that the two classes are external, I placed them in a separate module, as shown:
```python
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
```
The client only knows how to call the `execute()` method, and it has no idea about the `play()` or `speak()`. Adapters to the rescue! I created a generic `Adapter` class that allows to adapt a number of objects with different interfaces, into one unified interface. The `obj()` argument of the `__init__()` method is the object that I want to adapt, and `adapted_methods` is a dictionary containing key/value pairs of method the client calls/method that should be called.
```python
class Adapter:
	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self.obj)
```
An `objects` list holds all the objects. The compatible objects that belong to the `Computer` class need no adaptation. I added them directly to the list. The incopatible objects are not added directly. They are adapted using the `Adapter` class. The result is that the client code can continue using the known `execute()` method on all objects without the need to be aware of any interface differences between the used classes.
```python
def check_electronics_main(type_electronics, customer):
	objects = [Computer(type_electronics)]
	device = Electronic_device(type_electronics)
	objects.append(Adapter(device, dict(execute=device.play)))
	human = Human(customer)
	objects.append(Adapter(human, dict(execute = human.speak)))

	for i in objects:
		print('{} {}'.format(str(i), i.execute()))
```

__5. After checking the functionality of the device, the user has the oportunity to put some covers on his/her, for example: stickers or plastic cover. This is done via the Decorator pattern (`decorator.py`). Initially, there is only the `Device`, but there can be applied covers `stickers` and `plastic`. So, there is created separate wrapper classes for each function like `Stickers` and `PlasticCover`. First, it is called `Stickers` class, then the `PlasticCover` class.
```python
class PlasticCover(Device):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "{} in plastic cover".format(self._wrapped.render())

class Stickers(Device):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "{} with stickers".format(self._wrapped.render())
```

The `apply_cover_main()` function shows how the Decorator pattern can be used by the client code. The client code creates an instance of the `Device` class and uses it to apply different covers. Let's consider the following code:
```python
def apply_cover_main(device, cover_type):

	device_zero = Device(device)
	if cover_type == 'p':
		device_after = PlasticCover(device_zero)
	elif cover_type == 's':
		device_after = Stickers(device_zero)
	elif cover_type == 'b':
		device_after = PlasticCover(Stickers(device_zero))

	#return device_after.render()
	#print("before :", device_zero.render())
	time.sleep(1)
	print(device_after.render())
```


__6. After the customer selected the type of device and checked if it works and applied some covers, he/she should pay for it. In order to simulate the paying process the amount of money which must be payed is a random number, like the discount percents. This can be done via a special service developed. This service represents a Proxy pattern. The service provides 3 options:__
	* Checking if customer has discount: This operation does not require special privileges
	* Adding a new user: This operation requires the client to provide a special secert message
	* Paying for the device: This operation does not require special privileges

The `SensitiveInfo` class contains the information that need to be protected. The `users` variable is the list of existing users. The `read()` method prints the list of the users. The `add()` method adds a new user to the list. Let's consider the following code:
```python
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
```
The `Info` class is a protection proxy of `SensitiveInfo`. The `secret` variable is the message required to be known/provided by the client code to add a new user. Note that this is just ane exmple. In reality, this should never happen.

The `read()` method is a wrapper to `SensitiveInfo.read()`. The `add()` method ensures that a new user can be added only if the client code knows the secret message. Let's consider the following code:
```python
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
```
The `discount_main()` function shows how the Proxy pattern can be used by the client code. The client code creates an instance of the `Info` class and uses the displayed menu to check if person has discount, add a new user, or just pay for the device. Let's consider the following code:
```python
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
```

 

All 3 creational and 3 structural patterns are called by `main.py` code, which is responsible also for reading the input from the customer.
```python
if __name__ == '__main__':
		
	customer = input("What's your full name? (First_Name Last_Name) ")

	zakaz = True
	while zakaz:	
		electronics_style = input('What piece of electronics would you like, [m]ac, [d]esktop or [n]otebook? ')
		print('\n')
		if electronics_style != 'm' and electronics_style != 'd' and electronics_style != 'n':
			print('Sorry, only Mac Air 13 (key m), Desktop (key d) and Notebook (key n) are available', end = '\n')
		else:
			zakaz = False
	
	if electronics_style == 'd':
		desktop_main()

		check_answer = input('Do you want to check your desktop? [y]es, [n]o : ')
		print('')
		if check_answer == 'y':
			check_electronics_main('Desktop', customer)
			print('')
		cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your desktop? ')
		print()
		if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
			apply_cover_main('Desktop', cover_answer)
			print('')
		price = random.randint(500, 4000)
		discount = random.randint(0, 20)
		discount_main(price, discount, customer)

	elif electronics_style == 'm':
		mac_main()

		check_answer = input('Do you want to check your mac? [y]es, [n]o : ')
		print('')
		if check_answer == 'y':
			check_electronics_main('Mac', customer)
			print('')
		cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your mac? ')
		print()
		if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
			apply_cover_main('Mac', cover_answer)
			print('')
		price = random.randint(500, 4000)
		discount = random.randint(0, 20)
		discount_main(price, discount, customer)

	elif electronics_style == 'n':
		main_notebook()

		check_answer = input('Do you want to check your notebook? [y]es, [n]o : ')
		print('')
		if check_answer == 'y':
			check_electronics_main('Notebook', customer)
			print('')
		cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your notebook? ')
		print()
		if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
			apply_cover_main('Notebook', cover_answer)
			print('')
		price = random.randint(500, 4000)
		discount = random.randint(0, 20)
		discount_main(price, discount, customer)

	print('Enjoy your monster!')
```

## Results

Here is ilustrated the results for differet type of inputs:
* Apple Mac Air
```bash
$ python main.py
What's your full name? (First_Name Last_Name) Alex Clefos
What piece of electronics would you like, [m]ac, [d]esktop or [n]otebook? m


inserting RAM ...
putting SSD ...
installing the GPU ...
preparing last details ...
your Mac Air is ready!

Model: 3.2GHz Mac Air
Memory: 16Gb
SSD: 256Gb
Graphics Card: Apple M1 8-core chip

Do you want to check your mac? [y]es, [n]o : y

The Mac executes a program
The Mac  is playing an electronic song!
Alex Clefos the customer : Wow it works!

Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your mac? n

1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 2
What is the secret word? TMPS==design_patterns
Added user Alex Clefos
1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 3
Alex Clefos , good news, you have 12 % discount!
Alex Clefos , you have to pay 1444.08 !
Enjoy your monster!
```
	
* Desktop

```bash
$ python main.py
What's your full name? (First_Name Last_Name) Dima Trubca
What piece of electronics would you like, [m]ac, [d]esktop or [n]otebook? d


What is the size of the SSD (in Gb)?  512
What is the ram memory (in Gb)? 12
What is the GPU in your desktop? GeForce RTX 2080 Ti


inserting RAM ...
putting SSD ...
installing the GPU ...
preparing last details ...
your personalized Desktop is ready!

Memory: 12Gb
SSD: 512Gb
Graphics Card: GeForce RTX 2080 Ti
Do you want to check your desktop? [y]es, [n]o : n

Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your desktop? b

Desktop with stickers in plastic cover

1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 1
Dima Trubca does not have discount!
1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 3
Dima Trubca , unfortunately, you do not have a discount!
Dima Trubca , you have to pay 2128 !
Enjoy your monster!
```

* Notebook

```bash
$ python main.py
What's your full name? (First_Name Last_Name) Mihai Moglan
What piece of electronics would you like, [m]ac, [d]esktop or [n]otebook? n


Do you need an [o]ffice or [g]aming notebook? g


inserting RAM ...
putting SSD ...
installing the GPU ...
preparing last details ...
your personalized Notebook is ready!

Memory: 16Gb
SSD: 1024Gb
Graphics Card: NVidia GeForce RTX 3080 Ti
Do you want to check your notebook? [y]es, [n]o : y

The Notebook executes a program
The Notebook  is playing an electronic song!
Mihai Moglan the customer : Wow it works!

Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your notebook? s

Notebook with stickers

1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 1
Mihai Moglan has discount!
1. Check person has discount |==| 2. Add a new person |==| 3. Pay
Choose option: 3
Mihai Moglan , good news, you have 20 % discount!
Mihai Moglan , you have to pay 1329.6000000000001 !
Enjoy your monster!
```

