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