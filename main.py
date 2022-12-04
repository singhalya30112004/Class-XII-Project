from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import onetimepad
#import rsa
#from cryptography.fernet import Fernet

#Root window and mainframe settings
root = Tk()
root.title("Cryptik")
root.minsize(width=150, height=300)
root['bg'] = 'white'
s = ttk.Style()
s.configure('Mainframe.TFrame', background='white')
mainframe = ttk.Frame(root, padding="3 3 12 12", style="Mainframe.TFrame")
mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
root.columnconfigure(0, weight  = 1)
root.rowconfigure(0, weight = 1)

#Logo settings
s.configure('label.TLabel', background="white")
logo = ttk.Label(mainframe, style="label.TLabel")
image = Image.open("logo.png")
resize_image = image.resize((150,50))
img = ImageTk.PhotoImage(resize_image)
logo['image'] = img
logo.grid(column=2, row=1, sticky=(W, E))

#User input field
s.configure('Entry.TEntry', background="white")
inputString = StringVar()
textInput = ttk.Entry(mainframe, textvariable=inputString, style='Entry.TEntry')
textInput.grid(column = 2, row = 2, sticky=(W,E))

#Placeholder text for user input
textInput.insert(0, 'Enter a string')
textInput.configure(state=DISABLED)
def on_click(event):
    textInput.configure(state=NORMAL)
    textInput.delete(0, END)
textInput.bind("<Button-1>", on_click)

#OR label
s.configure('orLabel.TLabel', background="white", font="none 10")
orLabel = ttk.Label(mainframe, text="or", style="orLabel.TLabel")
orLabel.grid(column=2, row=3, sticky=(W, E))
orLabel.config(anchor=CENTER)

#File upload
def UploadAction(event=None):
    global filePath
    filePath = filedialog.askopenfilename()
    #Display file name rather than full path
    breakFile = filePath.split("/")
    fileButton.configure(text=breakFile[-1])
    print('Selected:', filePath)
fileButton = ttk.Button(mainframe, text='Select a file', command=UploadAction)
fileButton.grid(column= 2, row = 4, sticky=(W,E))

#Dropdown menu 
choices = StringVar()
dropdown = ttk.Combobox(mainframe, textvariable=choices)
dropdown['values'] = ('One Time Pad', 'Reverse', 'XOR', 'Atbash', 'Caeser')
dropdown.state(["readonly"])
dropdown.grid(column=2, row=5, sticky=(W,E))

#Radiobuttons
s.configure('buttons.TRadiobutton', background="white")
encryptOrDecrypt = StringVar()
encrypt = ttk.Radiobutton(mainframe, text='Encrypt', variable=encryptOrDecrypt, value='encrypt', style='buttons.TRadiobutton')
encrypt.grid(column=2, row=6, sticky=(W,E))
decrypt = ttk.Radiobutton(mainframe, text='Decrypt', variable=encryptOrDecrypt, value='decrypt', style='buttons.TRadiobutton')
decrypt.grid(column=2, row=7, sticky=(W,E))

#Initiate program on button submit
def main():
    #Initializing inputs
    text = inputString.get()
    fileName= fileButton.cget('text')
    processChoice = encryptOrDecrypt.get()
    algorithmChoice = dropdown.get()
    
    #Get filetype
    fileTypes = fileName.split('.')
    fileExtension = fileTypes[-1]
    #Input error checks
    if (text == "Enter a string" or text == "") and (fileName == "Select a file" or fileName == ""):
        print("SUBMIT ERROR: Please provide input and try again")
        quit()
    elif (text != "Enter a string" and text != "") and (fileName != "Select a file" and fileName != ""):
        print("SUBMIT ERROR: Please provide only one input and try again")
        quit()
    elif algorithmChoice == "":
        print("SUBMIT ERROR: Please choose an algorithm and try again")
        quit()
    elif processChoice == "": 
        print("SUBMIT ERROR: Please specify encryption or decryption and try again")
        quit()
    #Checking if input is string or file
    elif text != "Enter a string" and text != "":
        userInput = 'string'
    elif fileName != "Select a file" and fileName != "":
        userInput = 'file'

    #Checking for algorithm
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
            
    if algorithmChoice == 'One Time Pad':
        if processChoice == 'encrypt':
            if userInput == 'string':
                encryptedMessage = onetimepad.encrypt(text, 'random')
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
                        encryptedFile.write(onetimepad.encrypt(line, 'random'))
                        encryptedFile.write('\n')
                    encryptedFile.close()
                    enc = ttk.Label(mainframe, text= "Encrypted file saved", style="orLabel.TLabel")
                    enc.grid(column=2, row=9, sticky=(W,E))
        else: 
            if userInput == 'string':
                decryptedMessage = onetimepad.decrypt(text, 'random')
                
                enc = ttk.Label(mainframe, text= "Decrypted message is: ", style="orLabel.TLabel")
                enc.grid(column=2, row=9, sticky=(W,E))
                output = ttk.Entry(mainframe)
                output.grid(column=2, row=10, sticky=(W,E))
                output.insert(0, decryptedMessage)
                output.configure(state="readonly")
            elif userInput == 'file':
                with open(filePath, 'r') as myfile:
                    encryptedFile = open((filePath[:len(filePath) - len(fileName)] + fileName + '_decrypted' + '.' + fileExtension), 'x')
                    for line in myfile:
                        encryptedFile.write(onetimepad.decrypt(line[:-1], 'random'))
                        encryptedFile.write('\n')
                    encryptedFile.close()
                    enc = ttk.Label(mainframe, text= "Decrypted file saved", style="orLabel.TLabel")
                    enc.grid(column=2, row=9, sticky=(W,E))
            
    '''elif algorithmChoice == 'Reverse':
        if processChoice == 'encrypt':
            #do something
        else: 
            #do something else
    elif algorithmChoice == 'XOR':
        if processChoice == 'encrypt':
            #do something
        else: 
            #do something else
    elif algorithmChoice == 'Atbash':
        if processChoice == 'encrypt':
            #do something
        else: 
            #do something else
    elif algorithmChoice == 'Caeser':
        if processChoice == 'encrypt':
            #do something
        else: 
            #do something else'''

button = ttk.Button(mainframe, text='Submit', command=main)
button.grid(column=2, row=8, sticky=(W,E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()