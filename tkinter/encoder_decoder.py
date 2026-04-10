from tkinter import *
import time

window = Tk()
window.geometry("1200x680")
window.update()

window.config(bg="#F9EAEA")

def encode():
    message = encode_entry.get()
    encoded_text = ""
    for letter in message:
        encoded_text += chr(ord(letter)+1)
    encode_output.config(text=encoded_text)

def decode():
    message = decode_entry.get()
    decoded_text = ""
    for letter in message:
        decoded_text += chr(ord(letter)-1)
    decode_output.config(text=decoded_text)

def copy_message(type):
    window.clipboard_clear()
    if type == "encode":
        window.clipboard_append(encode_output.cget("text"))
    else:
        window.clipboard_append(decode_output.cget("text"))
    window.update()



Label(window, font=("Saint Serif", 48), underline=0, text="Encode a message").place(relx=0.25,rely=0.15, anchor=CENTER)

encode_frame = Frame(window)
encode_frame.place(relx=0.25,rely=0.6, anchor=CENTER, width=window.winfo_width()//2-80, height=window.winfo_height()//8)
encode_frame.update()

encode_entry = Entry(encode_frame, font=("Saint Serif", 32))
encode_entry.place(x=0,y=0, width=encode_frame.winfo_width()-80, height=encode_frame.winfo_height())
encode_entry.update()

encode_output = Label(window, font=("Saint Serif", 32), bd=4, relief="solid", bg="#F8F8F8")
encode_output.place(relx=0.25, rely=0.3, anchor=CENTER, height=window.winfo_height()//8, width=window.winfo_width()//3)

encode_btn = Button(encode_frame, text="Copy an encoded message", wraplength=80, command=lambda: copy_message("encode"))
encode_btn.place(x=encode_frame.winfo_width()-78,y=0, width=80, height=encode_frame.winfo_height())


separator = Label(window, bg="#000000")
separator.place(anchor=CENTER, x=window.winfo_width()//2, y=window.winfo_height()//2, width=8, height=window.winfo_height())


Label(window, font=("Saint Serif", 48), underline=0, text="Decode a message").place(relx=0.75,rely=0.15, anchor=CENTER)

decode_frame = Frame(window)
decode_frame.place(relx=0.75,rely=0.6, anchor=CENTER, width=window.winfo_width()//2-80, height=window.winfo_height()//8)
decode_frame.update()

decode_entry = Entry(decode_frame, font=("Saint Serif", 32))
decode_entry.place(x=0,y=0, width=encode_frame.winfo_width()-80, height=encode_frame.winfo_height())
decode_entry.update()

decode_output = Label(window, font=("Saint Serif", 32), bd=4, relief="solid", bg="#F8F8F8")
decode_output.place(relx=0.75, rely=0.3, anchor=CENTER, height=window.winfo_height()//8, width=window.winfo_width()//3)

decode_btn = Button(decode_frame, text="Copy a decoded message", wraplength=80, command=lambda: copy_message("decode"))
decode_btn.place(x=decode_frame.winfo_width()-78,y=0, width=80, height=encode_frame.winfo_height())


def update_text():
    encode()
    decode()
    window.after(10, update_text)
update_text()

window.mainloop()
