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
