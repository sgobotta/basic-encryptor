from Crypto.Cipher import AES
from Crypto import Random
import random
import base64
import hashlib

#@author Santiago Botta

class Encryptor:

	def __init__(self, key):
		self.block_size = 32
		self.key 				= hashlib.sha256(key.encode()).digest()

	'''
		Purpose: 			Given a string containing a message returns a byte string that represents a decoded message
		Precondition: 'message' must be a string
	'''
	def encrypt(self, message):
		iv 				 = self.generate_iv()
		obj 			 = AES.new(self.key, AES.MODE_CBC, iv)
		message 	 = self.pad(message)
		ciphertext = obj.encrypt(message)
		return base64.b64encode(iv + ciphertext)

	'''
		Purpose: 			Given a byte string returns a string that represents an encoded message
		Precondition: 'ciphertext' must be a byte string
	'''
	def decrypt(self, ciphertext):
		ciphertext = base64.b64decode(ciphertext)
		iv 				 = ciphertext[:AES.block_size]
		obj 			 = AES.new(self.key, AES.MODE_CBC, iv)
		message 	 = obj.decrypt(ciphertext[AES.block_size:]).decode('utf-8')
		return self.unpad(message)

	'''
		Purpose: 	Given a string containing a message, appends as many characters as
							needed to satisfy the AES API and returns a new string
		Precondition: 'message' must be a string
	'''
	def pad(self, message):
		pad 		= self.block_size - (len(message) % self.block_size)
		charpad = chr(self.block_size - len(message) % self.block_size)
		message = message + pad * charpad
		return message

	'''
		Purpose: 			Given a string containing a message, reduces it's last characters to 
									fix the original message and returns a new string
		Precondition:	'message' must be a string 
	'''
	def unpad(self, message):
		charpad = message[len(message)-1:]
		return message[:-ord(message[len(message)-1:])]

	'''
		Purpose:			Returns a randomly generated initialization vector
		Precondition: None
	'''
	def generate_iv(self):
		return Random.new().read(AES.block_size)



"""
    An encryptor should have:
        - define a block size for iv extraction
        - define a key

    Encryption should:
        - pad a raw text
        - generate IV reading the current MODE block size (16)
        - return the IV plus the encrypted raw input (preferably post base64 encoded)

    Decryption should:
        - get the cipher text (decode base64 if the input was encoded)
        - get the IV chars from the cipher string segment
        - use a new encriptor instance with the same key, the same MODE and the IV
        - return the unpadded decrypted segment of the given string (that might have been base64 decoded)
        * It might be necesary to decode to 'utf8'


    		messageLength = len(message)
    		if(messageLength % 16 != 0):
    				pad = [0]*(16 - messageLength % 16)
    				for i in range(0, 16 - messageLength % 16):
    						pad[i] = random.choice(string.ascii_letters)
    				message = message + ''.join(pad) * 

"""
