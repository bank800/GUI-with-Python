from tkinter import *
from random import randint

App = Tk()
App.title('App')
App.geometry('250x150')


def show_msg():
    msg = Label(App, text=randint(1, 100))
    msg.pack()


B = Button(App, text='Generate', command=show_msg)
B.pack()
App.mainloop()
