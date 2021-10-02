import time
from abstract_factory import main_notebook
from builder import desktop_main
from factory_method import mac_main

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
