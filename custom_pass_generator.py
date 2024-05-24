import random
import pyperclip
from tkinter import *

root = Tk()
root.geometry("800x400")
root.config(bg="#222")
pwd = StringVar()
password = StringVar()
pass_len = IntVar()
pass_len.set(0)


def generate_pass():
    # declaring arrays of the characters needed for the password
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['@', '#', '$', '%', '?', '/', '|', '*']

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    pass_list = [random.choice(numbers), random.choice(symbols)]

    # creating a customized password based on the users keyword
    keyword = ''.join(random.choice((str.upper, str.lower))(char) for char in password.get())
    keyword = keyword.replace("A", "4")
    keyword = keyword.replace("a", "@")
    keyword = keyword.replace("i", "1")
    keyword = keyword.replace("I", "!")
    keyword = keyword.replace("o", "0")
    pass_list += keyword

    for _ in range(pass_len.get() - len(keyword) - 2):
        if len(keyword) + 4 > pass_len.get():
            pass
        else:
            pass_list += random.choice(letters+numbers+symbols)

    custom_pass = ""
    for char in pass_list:
        custom_pass += char
    pwd.set(custom_pass)


def copy_clipboard():
    random_password = pwd.get()
    pyperclip.copy(random_password)


Label(root, text="Make your keyword a strong password", fg="#FDFAF0", bg="#222", font="Agrandir 30 bold").pack(pady=20)
Label(root, text="Enter keyword: ", fg="white", bg="#222").pack(pady=3)
Entry(root, textvariable=password).pack(pady=3)
Label(root, text="Enter desired length: ", fg="white", bg="#222").pack(pady=3)
Entry(root, textvariable=pass_len).pack(pady=3)
Button(root, text="Create new password", fg="white", bg="#F8AACF", command=generate_pass).pack(pady=7)
Entry(root, textvariable=pwd).pack(pady=7)
Button(root, text="Tap to copy clipboard", fg="white", bg="#F8AACF", command=copy_clipboard).pack()
root.mainloop()
