import os

verbose = True

class WriteFile:
	def __init__(self, path, txt):
		self.path, self.txt = path, txt

	def execute(self):
		if verbose:
			print("[adding new information to file '{}']".format(self.path))

		data = ''
		with open(self.path, mode = 'r', encoding = 'utf-8') as out_file:
			data = out_file.read()

		with open(self.path, mode = 'w', encoding = 'utf-8') as out_file:
			out_file.write(data + '\n' + self.txt)


class CreateFile:
	def __init__(self, path, txt = 'Hello\n'):
		self.path, self.txt = path, txt


	def execute(self):
		if verbose:
			print("[creating file '{}']".format(self.path))

		with open(self.path, mode = 'w', encoding = 'utf-8') as out_file:
			out_file.write(self.txt)

	def undo(self):
		delete_file(self.path)

class ReadFile:

	def __init__(self, path):
		self.path = path

	def execute(self):
		if verbose:
			print("[reading file '{}']".format(self.path))

		with open(self.path, mode = 'r', encoding = 'utf-8') as in_file:
			print(in_file.read(), end = '\n')


def delete_file(path):
	if verbose:
		print("deleting file '{}'".format(path))

	os.remove(path)


def command_main(orig_name, command, text):

	orig_name = 'C:\\Users\\hp\\Desktop\\UTM\\Lab3_TMPS\\' + orig_name 

	if command == 'create':
		cmd = CreateFile(orig_name)
		cmd.execute()
	if command == 'read':
		cmd = ReadFile(orig_name)
		cmd.execute()
	if command == 'write':
		cmd = WriteFile(orig_name, text)
		cmd.execute()
	if command == 'delete':
		cmd = CreateFile(orig_name)
		cmd.undo()
