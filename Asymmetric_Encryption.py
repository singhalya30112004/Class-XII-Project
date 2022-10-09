import rsa

publicKey, privateKey = rsa.newkeys(512)

print("Please enter a message: ", end='')
message = input()

encryptedMessage = rsa.encrypt(message.encode(), publicKey)
decryptedMessage = rsa.decrypt(encryptedMessage, privateKey).decode()

print('Encryption in process ... ')
print("Original message is:", decryptedMessage)
print("The encrypted message is:", encryptedMessage)
