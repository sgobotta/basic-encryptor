from aes import Encryptor
import cmd
import os
import sys
import time

#@author Santiago Botta

class Program(cmd.Cmd):

	prompt = "Encryptor >> "

	def __init__(self, argv):
		self.filepath 				= None
		self.file_extension 	= None
		self.command 					= None
		self.argv							= argv
		self.key 							= None
		self.output_extension = None
		self.output_mode 			= None
		self.valid_d_extns 		= [	'.crypt' ]
		self.valid_e_extns    = [	'.txt' ]
		self.single_commands  = [	'help' ]
		self.multi_commands   = [	'encrypt', 'decrypt' ]
		self.error_map        = {	'file_not_found': 	"File not found. Please check your file name and try again.",
															'invalid_file': 		'Unkown file extension. Accepted files: ' + ', '.join(self.valid_e_extns + self.valid_d_extns),
															'invalid_key': 			'Key is not valid!',
															'key_input': 				'Key must not be null. Please enter a numeric key',
															'decrypt_argument': "Command doesn't match file type.\nValid decryption files:\n    " + ', '.join(self.valid_d_extns),
															'encrypt_argument': "Command doesn't match file type.\nValid encryption files:\n    " + ', '.join(self.valid_e_extns)
														}
		self.error = "Error: "
		super().__init__()

	def set_key(self, key):
		self.key = key

	def validate_args(self):
		if len(self.argv) == 1:
			return self.show_help()
		elif len(self.argv) == 2:
			return self.show_help()
		elif len(self.argv) == 3:
			return True

	def validate_command(self):
		command = self.argv[1]
		if command == 'help':
			return self.show_help()
		if command == 'decrypt':
			self.output_extension = '.txt'
			self.output_mode = 'w'
		if command == 'encrypt':
			self.output_extension = '.crypt'
			self.output_mode = 'wb'
		if command not in self.multi_commands:
			return self.show_help()
		self.command = command
		return True

	def validate_file(self):
		file = self.argv[2]
		self.filepath, self.file_extension = os.path.splitext(file)
		if not self.validate_file_extension():
			self.show_error('invalid_file')
			return False
		else:
			return True

	def validate_file_extension(self):
		return self.file_extension in self.valid_e_extns + self.valid_d_extns
		
	def validate_execution(self):
		return self.validate_decryption() and self.validate_encryption()

	def validate_decryption(self):
		if self.command == 'decrypt' and self.file_extension not in self.valid_d_extns:
			self.show_error('decrypt_argument')
			return False
		return True

	def validate_encryption(self):
		if self.command == 'encrypt' and self.file_extension not in self.valid_e_extns:
			self.show_error('encrypt_argument')
			return False
		return True
		
	def validate_key(self, key):
		if key == '':
			self.show_error('key_input')
			return False
		return True

	def validate_file_existence(self):
		if not os.path.isfile(self.argv[2]):
			self.show_error('file_not_found')
			return False
		return True

	def read_file(self):
		data = open(self.filepath + self.file_extension, 'r')
		content = data.read()
		data.close()
		return content

	def parse_str(self, string):
		return string.replace("'", "'")

	def write_file(self, data):
		output_file = open(self.filepath + self.output_extension, self.output_mode)
		output_file.write(data)
		output_file.close()

	def execute(self):

		_input = self.read_file()
		_input = self.parse_str(_input)

		encryptor = Encryptor(self.key)
		func = getattr(encryptor, self.command)
		try: 
			output_content = func(_input)
		except UnicodeDecodeError:
			self.show_error('invalid_key')
			return False

		self.write_file(output_content)
		print("> Finished!\nOutput directory: " + self.filepath + self.output_extension)

	def show_help(self):
		print('Usage: encryptor <command>\n\n  where <command> is one of:\n    help\n    encrypt <argument>\n    decrypt <argument>\n  and <argument> is:\n    .txt file (encrypt)\n    .crypt file (decrypt)')
		return False

	def show_error(self, kind):
		print(self.error + self.error_map[kind])

	def exec_start(self):
		try: 
			key = str(input("Please provide a key for your file (numbers and letters)\n >>> "))
		except KeyboardInterrupt:
			print("\n\n\nAhww, watch your keystrokes... bye bye!\n\n")
			sys.exit()		
		return key

if __name__ == '__main__':

	logo = '''                                                   ``                                                                                                                                                    
                                `                                                                              

_______ _______          _________   _______  _        _______  _______           _______ _________ _______  _______ 
\__   __/(  ____ \|\     /|\__   __/  (  ____ \( (    /|(  ____ \(  ____ )|\     /|(  ____ )\__   __/(  ___  )(  ____ )
   ) (   | (    \/( \   / )   ) (     | (    \/|  \  ( || (    \/| (    )|( \   / )| (    )|   ) (   | (   ) || (    )|
   | |   | (__     \ (_) /    | |     | (__    |   \ | || |      | (____)| \ (_) / | (____)|   | |   | |   | || (____)|
   | |   |  __)     ) _ (     | |     |  __)   | (\ \) || |      |     __)  \   /  |  _____)   | |   | |   | ||     __)
   | |   | (       / ( ) \    | |     | (      | | \   || |      | (\ (      ) (   | (         | |   | |   | || (\ (   
   | |   | (____/\( /   \ )   | |     | (____/\| )  \  || (____/\| ) \ \__   | |   | )         | |   | (___) || ) \ \__
   )_(   (_______/|/     \|   )_(     (_______/|/    )_)(_______/|/   \__/   \_/   |/          )_(   (_______)|/   \__/
                                                                                                                       
                                                                                                                                                                
''' 


	def _next(boolean):
		if not boolean:
			sys.exit()

	def show_logo():
		for char in logo:
			time.sleep(0.0002)
			sys.stdout.write(char)
			sys.stdout.flush()

	os.system('cls' if os.name == 'nt' else 'clear')

	show_logo()

	program = Program(sys.argv)

	validation = program.validate_args()
	_next(validation)

	validation = program.validate_command()
	_next(validation)

	validation = program.validate_file()
	_next(validation)

	validation = program.validate_execution()
	_next(validation)

	validation = program.validate_file_existence()
	_next(validation)



	print("Selected file: " + sys.argv[2])
	print("Selected mode: " + sys.argv[1])
	print("\n")

	key = program.exec_start()

	validation = program.validate_key(key)
	_next(validation)

	program.set_key(key)
	program.execute()
	_next(1)
