print("Please enter a message: ", end='')
message = input()
encryptedMessage = ''


i = len(message) - 1

print('Encryption in process ... ')
print("Original message", message)

while i >= 0:
    encryptedMessage = encryptedMessage + message[i]
    i = i - 1
print("The encrypted message is:", encryptedMessage)
