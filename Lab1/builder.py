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
		self.desktop = Desktop('XY8913548945')

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