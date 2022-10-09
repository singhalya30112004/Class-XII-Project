import onetimepad

print("Please enter a message: ", end='')
message = input()

encryptedMessage = onetimepad.encrypt(message, 'random')
decryptedMessage = onetimepad.decrypt(encryptedMessage, 'random')

print('Encryption in process ... ')
print("Original message is:", decryptedMessage)
print("The encrypted message is:", encryptedMessage)
