import unittest
from encryptor import Program

class TestEncryptor(unittest.TestCase):

	def setUp(self):

		self.txt_arg   = 'test/test.txt'
		self.crypt_arg = 'test/test.crypt'

		# No arguments passed
		self.argv	= ['encryptor.py']

		# Correct use of command and arguments
		self.encrypt_program = self.argv + ['encrypt', self.txt_arg]
		self.decrypt_program = self.argv + ['decrypt', self.crypt_arg]

		# Mixed up command and arguments
		self.failed_encrypt_program = self.argv + ['encrypt', self.crypt_arg]
		self.failed_decrypt_program = self.argv + ['decrypt', self.txt_arg]

		# Unkown command program
		self.unkown_command_program = self.argv + ['break', 'a.txt']

		# Unkown file extension program
		self.unkown_extension_program = self.argv + ['encrypt', 'something.weird']

		# Unkown file program
		self.file_not_found_program = self.argv + ['encrypt', 'i_dont_exist.txt']

		self.program = Program(self.argv)

	def tearDown(self):
		self.program = None

	def test_when_a_program_executes_with_no_arguments_false_is_returned_on_validate_args(self):
		self.assertEqual(False, self.program.validate_args())

	def test_when_a_program_executes_with_one_argument_false_is_returned_on_validate_args(self):
		self.program = Program(self.argv+['encrypt'])
		self.assertEqual(False, self.program.validate_args())

	def test_when_a_program_executes_with_two_arguments_true_is_returned_on_validate_args(self):
		self.program = Program(self.encrypt_program)
		self.assertEqual(True, self.program.validate_args())

	def test_when_help_command_is_passed_false_is_returned_on_validate_command(self):
		self.program = Program(self.argv+['help'])
		self.assertEqual(False, self.program.validate_command())
		self.assertIsNone(self.program.command)

	def test_when_encrypt_command_is_passed_the_program_variables_are_set_to_decrypt_mode_and_true_is_returned_on_validate_command(self):
		self.program = Program(self.decrypt_program)
		self.assertEqual(True, self.program.validate_command())
		self.assertEqual('decrypt', self.program.command)
		self.assertEqual('.txt', self.program.output_extension)
		self.assertEqual('w', self.program.output_mode)

	def test_when_decrypt_command_is_passed_the_program_variables_are_set_to_encrypt_mode_and_true_is_returned_on_validate_command(self):
		self.program = Program(self.encrypt_program)
		self.assertEqual(True, self.program.validate_command())
		self.assertEqual('encrypt', self.program.command)
		self.assertEqual('.crypt', self.program.output_extension)
		self.assertEqual('wb', self.program.output_mode)

	def test_when_unkown_command_is_passed_the_program_returns_false_on_validate_command(self):
		self.program = Program(self.unkown_command_program)
		self.assertEqual(False, self.program.validate_command())
		self.assertIsNone(self.program.command)

	def test_when_unkown_extensions_are_passed_the_program_returns_false_on_validate_file(self):
		self.program = Program(self.unkown_extension_program)
		self.assertEqual(False, self.program.validate_file())

	def test_when_known_extension_is_passed_the_program_returns_true_on_validate_file(self):
		self.program = Program(self.encrypt_program)
		self.assertEqual(True, self.program.validate_file())

	def test_when_extension_is_unkown_false_is_returned_on_validate_file_extension(self):
		self.program = Program(self.unkown_extension_program)
		self.assertEqual(False, self.program.validate_file_extension())

	def test_when_a_key_is_not_provided_program_returns_false_on_validate_key(self):
		self.program = Program(self.encrypt_program)
		self.assertEqual(False, self.program.validate_key(''))

	def test_when_a_key_is_provided_program_returns_true_on_validate_key(self):
		self.program = Program(self.encrypt_program)
		self.assertEqual(True, self.program.validate_key('123'))

	def test_when_a_non_existent_file_is_provided_program_returns_false_on_validate_file_existence(self):
		self.program = Program(self.file_not_found_program)
		self.assertEqual(False, self.program.validate_file_existence())

	def test_when_an_existent_file_is_provided_program_returns_true_on_validate_file_existence(self):
		self.program = Program(self.decrypt_program)
		self.assertEqual(True, self.program.validate_file_existence())


if __name__ == '__main__':
	unittest.main()
