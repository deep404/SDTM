import time

class Device:

	def __init__(self, device):
		self._device = device

	def render(self):
		return self._device

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

#if __name__ == '__main__':
#	apply_cover_main('ASUS', 'both')