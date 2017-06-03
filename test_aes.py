import unittest
from aes import Encryptor

class TestEncryptor(unittest.TestCase):

	def setUp(self):
		self.encryptor = Encryptor("1234567890123456")
		self.rawtext = "AES (Advanced Encryption Standard) is a symmetric block cipher standardized by NIST . It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long."

	def tearDown(self):
		self.encryptor = None

	def test_encryptor_encrypts_a_message_on_encrypt(self):
		cipheredoutput = self.encryptor.encrypt(self.rawtext)
		decodedmsg = self.encryptor.decrypt(cipheredoutput)
		self.assertEqual(self.rawtext, decodedmsg)

	def test_encryptor_decrypts_a_message_on_decrypt(self):
		cipheredinput = b'U2buuZLDdi+0zbWuSACRjRFt58Hj1hagV5nXUgqQZmhz9uccmtNHTsbWw2pDRmT7IlGVS69tKJ3hU1q6PajbGhMBOn2P/OWDF6MaagwLeGkTDiHHJm3M+A6QQ9Oy//AWhGhjHrXZpK5KxfJn9adWFmBxb4QkhYyeQRP2JsEnJKRlC3PUY+nmSoOMYN5HDAsTmM7KRzBArrrLDFbkeQIw1LGrgkW0PZsZzVT/5j/T4FvtEfiqjyU05k2cpasjGXt4EvDNWf7m/pIQfkZVrqKqJg=='
		decodedmsg = self.encryptor.decrypt(cipheredinput)
		self.assertEqual(self.rawtext, decodedmsg)

	def test_encryptor_generates_a_16_length_string_on_generate_iv(self):
		string = self.encryptor.generate_iv()
		self.assertEqual(16, len(string))

	def test_encryptor_pads_a_8_length_string_on_pad(self):
		message = self.encryptor.pad("ShortMsg")
		self.assertEqual(len(message) % 16, 0)
		self.assertEqual(message[:8], "ShortMsg")

	def test_encryptor_pads_a_18_length_string_on_pad(self):
		message = self.encryptor.pad("ALargerMessageeeee")
		self.assertEqual(len(message) % 16, 0)
		self.assertEqual(message[:18], "ALargerMessageeeee")

	def test_encryptor_pads_a_16_length_string_on_pad(self):
		message = self.encryptor.pad("A simple message")
		self.assertEqual(len(message) % 16, 0)
		self.assertEqual(message[:16], "A simple message")

if __name__ == '__main__':
	unittest.main()
