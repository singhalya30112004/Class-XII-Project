from optparse import Option
from cryptography.fernet import Fernet

message = input("Please enter a string: ")

option = input(
    "What do you want to do, encryption (type 'enc') or decryption (type 'dec') or both (type 'both'): ")
option.lower()

key = Fernet.generate_key()

fernet = Fernet(key)

encryptedMessage = fernet.encrypt(message.encode())
decryptedMessage = fernet.decrypt(encryptedMessage).decode()


if option == 'enc':
    print('You have selected to encrypt your message. \n Encryption in process ... ')
    print("Original string: ", message)
    print("Encrypted string: ", encryptedMessage)

elif option == 'dec':
    print('You have selected to decrypt your message. \n Decryption in process ... ')
    print("Original string: ", message)
    print("Decrypted string: ", decryptedMessage)

elif option == 'both':
    print('You have selected to both encrypt and decrypt your message. \n Conversion in process ... ')
    print("Original string: ", message)
    print("Encrypted string: ", encryptedMessage)
    print("Decrypted string: ", decryptedMessage)

else:
    print('Invalid Input')
