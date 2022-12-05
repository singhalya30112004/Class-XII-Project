import rsa

publicKey, privateKey = rsa.newkeys(512)

print("Please enter a message: ", end='')
message = input()

encryptedMessage = rsa.encrypt(message.encode(), publicKey)
decryptedMessage = rsa.decrypt(encryptedMessage, privateKey).decode()

print('Encryption in process ... ')
print("Original message is:", decryptedMessage)
print("The encrypted message is:", encryptedMessage)

'''if algorithmChoice == 'RSA':
        if processChoice == 'encrypt':
            publicKey, privateKey = rsa.newkeys(512)
            if userInput == 'string':
                encryptedMessage = rsa.encrypt(text.encode(), publicKey)

                #Displaying encrypted message
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
                        encryptedFile.write(str(rsa.encrypt(line.encode(), publicKey)) +'\n')
                    encryptedFile.close()
                    enc = ttk.Label(mainframe, text= "Encrypted file saved", style="orLabel.TLabel")
                    enc.grid(column=2, row=9, sticky=(W,E))

            #Displaying private key
            priv = ttk.Label(mainframe, text="Private key for decryption is: ", style="orLabel.TLabel")
            priv.grid(column=2, row=11, sticky=(W,E))
            dispkey = ttk.Entry(mainframe)
            dispkey.grid(column=2, row=12, sticky=(W,E))
            dispkey.insert(0, privateKey)
            dispkey.configure(state="readonly")

        else: 
            priv = ttk.Label(mainframe, text="Private key for decryption is: ", style="orLabel.TLabel")
            priv.grid(column=2, row=9, sticky=(W,E))
            s.configure('Entry.TEntry', background="white")
            pKey = StringVar()
            privKey = ttk.Entry(mainframe, textvariable=pKey, style='Entry.TEntry')
            privKey.grid(column = 2, row = 10, sticky=(W,E))

            if userInput == 'string':
                decryptedMessage = rsa.decrypt(bytes(text), bytes(privKey.get())).decode()
                enc = ttk.Label(mainframe, text= "Decrypted message is: ", style="orLabel.TLabel")
                enc.grid(column=2, row=11, sticky=(W,E))
                output = ttk.Entry(mainframe)
                output.grid(column=2, row=12, sticky=(W,E))
                output.insert(0, decryptedMessage)'''
