import pandas as pd
import tkinter as tk

encryptionkey = pd.read_csv(r"csvfile.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

original_message = 'It is a beautiful day to code something new. In fact, a day like any other,' \
                   ' with new projects and ideas. Maybe also new challenges and nerve-rackings bugs. Time will tell.'


def code_message(message):
    message_split = [char for char in message]
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]

        except:
            print('unrecognized character')
            coded_char = '@@@'
        coded_message = coded_message + coded_char
    return coded_message


def decode_message(message):
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]
        df2 = index_nb['Character'].tolist()
        s = [str(x) for x in df2]
        decoded_message = decoded_message + s
    new_word = ''.join(decoded_message)

    return new_word


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
    root.minsize(width=300, height=230)
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