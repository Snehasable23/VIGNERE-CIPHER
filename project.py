# -- coding: utf-8 --

# import tkinter module
from tkinter import *
from random import *
import tkinter as tk

# creating window object
window = Tk()

# defining size of window
window.geometry("800x400")

# setting up the title of window
window.title("Message Encryption and Decryption")

## setting the background color

window.configure(bg = 'dim gray')


rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
    window.destroy()

# Function to reset the window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# adding entries
entry_the_text = Entry(window, width = 30, textvariable = Msg)
entry_the_text.place(x = 200, y = 160)

entry_key = Entry(window, width = 30, textvariable = key)
entry_key.place(x = 200, y = 200)

entry_ED = Entry(window, width = 30, textvariable = mode)
entry_ED.place(x = 400, y = 240)

entry_the_converted_text = Entry(window, width = 30, textvariable = Result)
entry_the_converted_text.place(x = 350, y = 360)


# labels
Label(window,text= 'VIGNERE CIPHER', bg = 'dim gray', fg = 'navy blue', font=('bold', 30)).place(x = 225, y = 30)
Label(window, text = 'Enter the Text:', bg = 'dim gray', fg = 'white', font=('bold', 15)).place(x = 50, y = 160)
Label(window, text = 'Key:',bg = 'dim gray', fg = 'white', font = ('bold', 15)).place(x = 50, y = 200)
Label(window, text = 'e for Encrypt / d for Decrypt',bg = 'dim gray', fg = 'white', font=('bold', 15)).place(x = 50, y = 240)
Label(window, text = 'The Converted Text is:',bg = 'dim gray', fg = 'white', font = ('bold', 15)).place(x = 50, y = 360)

# Vigen?re cipher
import base64

# Function to encode
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                    ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                        ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))
## adding buttons

btn_Show_message  = Button( fg = "black",
                        font = ('arial', 16, 'bold'), width = 12,
                    text = "Show Message", bg = "green", command = Ref).place(x = 50, y = 280 )



btn_reset = Button( fg = "black",
                        font = ('arial', 16, 'bold'), width = 12,
                    text = "Reset", bg = "yellow", command = Reset).place(x = 280, y = 280 )



btn_exit = Button( fg = "black",
                        font = ('arial', 16, 'bold'), width = 12,
                    text = "Exit", bg = "red", command = qExit).place(x = 500, y = 280)

# keeps window alive
window.mainloop()
