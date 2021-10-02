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
