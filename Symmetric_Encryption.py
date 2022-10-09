from optparse import Option
from cryptography.fernet import Fernet

print("Please enter a message: ", end='')
message = input()

key = Fernet.generate_key()

fernet = Fernet(key)

encryptedMessage = fernet.encrypt(message.encode())
decryptedMessage = fernet.decrypt(encryptedMessage).decode()

print('Encryption in process ... ')
print("Original message is:", decryptedMessage)
print("The encrypted message is:", encryptedMessage)
