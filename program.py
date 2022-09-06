from optparse import Option
from cryptography.fernet import Fernet
import tkinter as tk

key = Fernet.generate_key()

fernet = Fernet(key)

def code_message(vx1):
    encryptedMessage = fernet.encrypt(vx1.encode())
    return encryptedMessage
    
def decode_message(vx2):
    decryptedMessage = fernet.decrypt(vx2.decode())
    return decryptedMessage

def GUI():
    def getResult():
        choice = v.get()
        if choice == 'e':

            x1 = entry1.get()
            label1['text'] = code_message(x1)
            canvas1.create_window(150, 200, window=label1)

        else:
            x1 = entry1.get()
            label1['text'] = decode_message(x1)
            canvas1.create_window(150, 200, window=label1)

    root = tk.Tk()
    root.title('EncryptINC')
    root.minsize(width=750, height=300)
    canvas1 = tk.Canvas(root, width=300, height=230)
    canvas1.pack()
    entry1 = tk.Entry(root)
    canvas1.create_window(150, 120, window=entry1)
    label1 = tk.Label()
    button1 = tk.Button(text='Submit', command=getResult)
    canvas1.create_window(150, 160, window=button1)

    v = tk.StringVar()
    v.set("e")

    b = tk.Radiobutton(root, text='Encrypt', variable=v, value='e')
    canvas1.create_window(150, 45, window=b)

    b2 = tk.Radiobutton(root, text='Decrypt', variable=v, value='d')
    canvas1.create_window(150, 70, window=b2)

    root.mainloop()


GUI()    