import json
from tkinter import *
from tkinter import scrolledtext
import requests

def pars():
    repo = txt.get()
    owner = "Automattic" 

    url = f"https://api.github.com/users/Automattic"
    repository_url = requests.get(url).json()

    try:
        repository_url['company']
        repository_url['email']
    except KeyError:
            repository_url['company'] = None
            repository_url['email'] = None

    with open("File.txt", "a+") as f:
        f.write(f"'company': '{repository_url['company']}'\n")
        f.write(f"'created_at': '{repository_url['created_at']}'\n")
        f.write(f"'email': '{repository_url['email']}'\n")
        f.write(f"'id': '{repository_url['id']}'\n")
        f.write(f"'name': '{repository_url['name']}'\n")
        f.write(f"'url': '{repository_url['url']}'\n")
        f.write("\n")
    with open("File.txt", "r+") as f1:
        line = f1.read()
        txt1.insert('1.0', line)

root = Tk()
root.title("JSONPars")
root.geometry('600x400')
lbl = Label(root, text="Введите имя репозитория")
lbl1 = Label(root, text="Например: Automattic  ")
lbl.grid(padx=150, pady=15)
lbl1.grid(padx=150, pady=15)
txt = Entry(root, width=50, justify="center")
txt.grid(padx=150, pady=15)
btn = Button(root, text="Нажать", command=pars)
btn.grid(padx=150, pady=15)
txt1 = scrolledtext.ScrolledText(root, height=10, width=50, bg='#000000', fg='#008000')
txt1.grid(padx=100, pady=15)
root.mainloop()
