# Creational Design Patterns Laboratory Work No1
## Author: Moglan Mihai, FAF - 192
------
## Introduction
__1. The topic behind this laboratory work is 'Management of electronics store', where the customer selects what type of electronic device he wants and for some gadgets he even selects the parameters for different parts.__

__2. The design patterns used in this laboratory work are:__
  * Factory Method
  * Abstract Factory
  * Builder

## Implementation & Explanation
In order to simulate the building of an electronic device is was used the function ```time.sleep()```.

The new computer analogy help to distinguish between a Builder pattern and a Factory pattern. If the customer decides to buy a specific preconfigured computer model, for example, the latest Apple 3.2 GHz Mac Air, it is used the Factory pattern. All the hardware specification are already predefined by the manufacturer, who knows what to do without consulting the customer. The manufacturer typically receives just a single instruction. Code-wise, this would look like the following (`factory_method.py`):
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

if __name__ == '__main__':
	mac_main()
```

Anoter option is buying a custop Desktop. In this case, is used the Builder pattern. The director gives orders to the manufacturer (builder) about the ideal computer specifications that were given by the customer. Code-wise, this looks like the following (builder.py):
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

if __name__ == '__main__':
	desktop_main()
```

The basic changes are the intoduction of a builder `DesktopBuilder`, a director `HardwareEngineer`, and the step-by-step construction of a desktop, which now supportts different configurations (cpu, gpu and ssd)


To Abstract Method was used in the creation of notebook. There are 2 types of notebooks office and gaming one. The main specifications for notebook remains the same: cpu, ssd and gpu. For every type of notebook the specifications classes are different:
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

All 3 creational patterns are called by `main.py` code, which is responsible also for reading the input from the customer.
```python
if __name__ == '__main__':
	
	zakaz = True
	while zakaz:	
		electronics_style = input('What piece of electronics would you like, [m]ac, [d]esktop or [n]otebook?')
		print('\n')
		if electronics_style != 'm' and electronics_style != 'd' and electronics_style != 'n':
			print('Sorry, only Mac Air 13 (key m), Desktop (key d) and Notebook (key n) are available', end = '\n')
		else:
			zakaz = False
	
	if electronics_style == 'd':
		desktop_main()	
	elif electronics_style == 'm':
		mac_main()
	elif electronics_style == 'n':
		main_notebook()
	print('Enjoy your monster!')
```

#### Run

```bash
$ # clone repository
$ py -m venv env # create env
$ env\Scripts\activate # activate env
$ pip install -r requirements.txt # install dependecies
$ py main.py # start the server
```

#### with docker

```bash
$ docker build --tag kitchen . # create kitchen image
$ docker network create nt # create docker network 
$ docker run -d --net nt --name kitchen kitchen # run docker container on created network
```
