from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

#Root window and mainframe settings
root = Tk()
root.title("Cryptik")
root.minsize(width=500, height=300)
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
resize_image = image.resize((200,75))
img = ImageTk.PhotoImage(resize_image)
logo['image'] = img
logo.grid(column=2, row=1, sticky=(W, E))

#User input field
s.configure('Entry.TEntry', background="white")
inputString = StringVar()
textInput = ttk.Entry(mainframe, textvariable=inputString, style='Entry.TEntry')
textInput.grid(column = 1, row = 2, sticky=(W))

#Placeholder text for user input
textInput.insert(0, 'Enter a string')
textInput.configure(state=DISABLED)
def on_click(event):
    textInput.configure(state=NORMAL)
    textInput.delete(0, END)
textInput.bind("<Button-1>", on_click)

#OR label
s.configure('orLabel.TLabel', background="white", font="none 14 bold")
orLabel = ttk.Label(mainframe, text="or", style="orLabel.TLabel")
orLabel.grid(column=2, row=2, sticky=(W, E))
orLabel.config(anchor=CENTER)

#File upload
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    #Display file name rather than full path
    breakFile = filename.split("/")
    fileButton.configure(text=breakFile[-1])
    print('Selected:', filename)
fileButton = ttk.Button(mainframe, text='Select a file', command=UploadAction)
fileButton.grid(column= 3, row = 2, sticky=(E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()