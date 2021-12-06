import time
import random

from domain.creational.abstract_factory import main_notebook
from domain.creational.builder import desktop_main
from domain.creational.factory_method import mac_main
from domain.structural.adapter_pattern import check_electronics_main
from domain.structural.decorator import apply_cover_main
from domain.structural.proxy_pattern import discount_main
from domain.behavioral.command import command_main

if __name__ == '__main__':
	
	orig_name = 'report.txt'
	command = 'create'
	command_main(orig_name, command, '')

	while True:	
		zakaz_text = ''
		customer = input("What's your full name? (First_Name Last_Name) ")

		zakaz_text += customer + '\n'


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

			zakaz_text += 'Desktop\n' 

			check_answer = input('Do you want to check your desktop? [y]es, [n]o : ')
			print('')
			if check_answer == 'y':
				zakaz_text += 'With check of desktop\n'
				check_electronics_main('Desktop', customer)
				print('')
			else:
				zakaz_text += 'Without check of desktop\n'
			cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your desktop? ')
			print()
			if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
				if cover_answer == 'b':
					zakaz_text += 'With plastic cover and stickers\n'
				elif cover_answer == 's':
					zakaz_text += 'With stickers\n'
				elif cover_answer == 'p':
					zakaz_text += 'With plastic cover\n'

				apply_cover_main('Desktop', cover_answer)
				print('')
			else:
				zakaz_text += 'Without covers\n'
			price = random.randint(500, 4000)
			discount = random.randint(0, 20)
			discount_main(price, discount, customer)

			command = 'write'
			command_main(orig_name, command, zakaz_text)

		elif electronics_style == 'm':
			mac_main()
			zakaz_text += 'Mac\n' 

			check_answer = input('Do you want to check your mac? [y]es, [n]o : ')
			print('')
			if check_answer == 'y':
				zakaz_text += 'With check of mac\n'

				check_electronics_main('Mac', customer)
				print('')
			else:
				zakaz_text += 'Without check of desktop\n'

			cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your mac? ')
			print()

			if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
				if cover_answer == 'b':
					zakaz_text += 'With plastic cover and stickers\n'
				elif cover_answer == 's':
					zakaz_text += 'With stickers\n'
				elif cover_answer == 'p':
					zakaz_text += 'With plastic cover\n'

				apply_cover_main('Mac', cover_answer)
				print('')
			else:
				zakaz_text += 'Without covers\n'

			price = random.randint(500, 4000)
			discount = random.randint(0, 20)
			discount_main(price, discount, customer)
			command = 'write'
			command_main(orig_name, command, zakaz_text)

		elif electronics_style == 'n':
			main_notebook()
			zakaz_text += 'Laptop\n'

			check_answer = input('Do you want to check your notebook? [y]es, [n]o : ')
			print('')
			if check_answer == 'y':
				zakaz_text += 'With check of laptop\n'

				check_electronics_main('Notebook', customer)
				print('')
			else:
				zakaz_text += 'Without check of desktop\n'

			cover_answer = input('Do you want to apply a [p]lastic, [s]tickers, [b]oth or [n]one cover on your notebook? ')
			print()
			if cover_answer == 's' or cover_answer == 'p' or cover_answer == 'b':
				if cover_answer == 'b':
					zakaz_text += 'With plastic cover and stickers\n'
				elif cover_answer == 's':
					zakaz_text += 'With stickers\n'
				elif cover_answer == 'p':
					zakaz_text += 'With plastic cover\n'

				apply_cover_main('Notebook', cover_answer)
				print('')
			else:
				zakaz_text += 'Without covers\n'

			price = random.randint(500, 4000)
			discount = random.randint(0, 20)
			discount_main(price, discount, customer)
			command = 'write'
			command_main(orig_name, command, zakaz_text)

		print('Enjoy your monster!')

		is_over = input('Is working day over? [y/n] ')
		if is_over == 'y':
			break


	print('\nToday report is: \n')
	command = 'read'
	command_main(orig_name, command, '')

	time.sleep(1)
	print('\nSending report on email...\n')

	time.sleep(1)
	print('\nDeleting local report...\n')
	command = 'delete'
	command_main(orig_name, command, '')

	time.sleep(1)
	print('\nDone! Have a nice day!')

