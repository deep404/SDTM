import time
import random

from domain.creational.abstract_factory import main_notebook
from domain.creational.builder import desktop_main
from domain.creational.factory_method import mac_main
from domain.structural.adapter_pattern import check_electronics_main
from domain.structural.decorator import apply_cover_main
from domain.structural.proxy_pattern import discount_main

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
