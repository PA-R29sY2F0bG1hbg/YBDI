from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

master = Tk()
master.geometry("550x300+300+150")
master.resizable(width=True, height=True)


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def open_img():
    x = "tmp/img-tmp.png"
    img = Image.open(x)
    # img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(master, image=img)
    panel.image = img
    panel.place(x=10, y=160)


btn = Button(master, text='open image', command=open_img).pack()

master.mainloop()
