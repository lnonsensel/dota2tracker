import tkinter, pywintypes
import time
from random import randint


def define_label(font_size = 10) -> tkinter.Label:
    font_size = str(font_size)
    label = tkinter.Label(text='waiting...', font=('Courier New',font_size), fg='red', bg='black')
    label.master.overrideredirect(True)
    label.master.geometry("+1+1")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))

    label.pack()
    return label 


def update_label(label: tkinter.Label, new_text: str):
    label.config(text = new_text)
    label.update()


if __name__ == '__main__':
    label = define_label(10)
    while True:
        update_label(label, str(randint(1,100)))
