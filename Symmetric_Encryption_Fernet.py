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

'''if algorithmChoice == 'Fernet':
        if processChoice == 'encrypt':
            key = Fernet.generate_key()
            fernet = Fernet(key)

            if userInput == 'string':
                encryptedMessage = fernet.encrypt(text.encode())

                enc = ttk.Label(mainframe, text= "Encrypted message is: ", style="orLabel.TLabel")
                enc.grid(column=2, row=9, sticky=(W,E))
                output = ttk.Entry(mainframe)
                output.grid(column=2, row=10, sticky=(W,E))
                output.insert(0, encryptedMessage)
                output.configure(state="readonly")
            elif userInput == 'file':
                with open(filePath, 'r') as myfile:
                    encryptedFile = open((filePath[:len(filePath) - len(fileName)] + fileName + '_encrypted' + '.' + fileExtension), 'x')
                    for line in myfile:
                        encryptedLine = fernet.encrypt(line.encode())
                        encryptedFile.write(str(encryptedLine))
                        encryptedFile.write('\n')
                    encryptedFile.close()
                    enc = ttk.Label(mainframe, text= "Encrypted file saved", style="orLabel.TLabel")
                    enc.grid(column=2, row=9, sticky=(W,E))
            
            priv = ttk.Label(mainframe, text="Key for decryption is: ", style="orLabel.TLabel")
            priv.grid(column=2, row=11, sticky=(W,E))
            dispkey = ttk.Entry(mainframe)
            dispkey.grid(column=2, row=12, sticky=(W,E))
            dispkey.insert(0, key)
            dispkey.configure(state="readonly")
        else: 
            priv = ttk.Label(mainframe, text="Key for decryption is: ", style="orLabel.TLabel")
            priv.grid(column=2, row=9, sticky=(W,E))
            s.configure('Entry.TEntry', background="white")
            pKey = StringVar()
            privKey = ttk.Entry(mainframe, textvariable=pKey, style='Entry.TEntry')
            privKey.grid(column = 2, row = 10, sticky=(W,E))

            fernet = Fernet(bytes(privKey.get()))

            if userInput == 'string':


                decryptedMessage = fernet.decrypt(bytes(text)).decode()
                enc = ttk.Label(mainframe, text= "Decrypted message is: ", style="orLabel.TLabel")
                enc.grid(column=2, row=11, sticky=(W,E))
                output = ttk.Entry(mainframe)
                output.grid(column=2, row=12, sticky=(W,E))
                output.insert(0, decryptedMessage)'''
