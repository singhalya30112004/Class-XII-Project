from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


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
    filename = filedialog.askopenfilename()
    #Display file name rather than full path
    breakFile = filename.split("/")
    fileButton.configure(text=breakFile[-1])
    print('Selected:', filename)
fileButton = ttk.Button(mainframe, text='Select a file', command=UploadAction)
fileButton.grid(column= 2, row = 4, sticky=(W,E))

#Dropdown menu 
choices = StringVar()
dropdown = ttk.Combobox(mainframe, textvariable=choices)
dropdown['values'] = ('RSA', 'Fernet', 'One Time Pad', 'Reverse', 'XOR', 'Atbash', 'Caeser')
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

    #Checking for algorithm
    if algorithmChoice == 'RSA':
        if processChoice == 'encrypt':
            output = ttk.Label(mainframe, text="sdsds", style="orLabel.TLabel")
            output.grid(column=2, row=9, sticky=(W,E))
        else: 
            output = ttk.Label(mainframe, text="sdsds", style="orLabel.TLabel")
            output.grid(column=2, row=9, sticky=(W,E))
    '''elif algorithmChoice == 'Fernet':
        if processChoice == 'encrypt':
            
        else: 
            
    elif algorithmChoice == 'One Time Pad':
        if processChoice == 'encrypt':
            
        else: 
            
    elif algorithmChoice == 'Reverse':
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