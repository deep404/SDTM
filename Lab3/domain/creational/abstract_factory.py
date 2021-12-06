import time

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

def main_notebook():
	notebook_type = validate_notebook()
	notebook = OfficeNotebook if notebook_type == 'o' else GamingNotebook
	environment = NotebookEnvironment(notebook)
	print(environment)

#if __name__ == '__main__':
#	main_notebook()