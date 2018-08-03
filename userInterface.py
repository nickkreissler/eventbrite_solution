import os
from work import Work
from tkinter import Tk, Label, Entry, Button,END
from random import *

class UserInterface(Tk):
    # set up the main window
    def __init__(self, parent='Tk'):
        Tk.__init__(self, parent)
        self.title('Play Craps')
        self.new_game()
        self.make_widgets()
    # when a new game is started, the firstRoll will start at 0
    def new_game(self):
        self.firstRoll = 0

    # create and place the widgets in the window
    def make_widgets(self):
        Label(self, text="Number of Workshops").grid(row=0, column=0, columnspan=1)
        Label(self, text="Max capacity of workshops").grid(row=0, column=1, columnspan=1)

        self.now = Entry(self)  # entry field for die 1
        self.ppw = Entry(self)  # entry field for die 2
        self.now.grid(row=1, column=0, columnspan=1)
        self.ppw.grid(row=1, column=1, columnspan=1)

        Label(self, text="Workshop Columns").grid(row=2, column=0, columnspan=1)
        Label(self, text="Input file path").grid(row=2, column=1, columnspan=1)
        Label(self, text="Output file Directory").grid(row=2, column=2, columnspan=1)

        self.wc = Entry(self)  # entry field for the first roll
        self.ip = Entry(self) 
        self.op = Entry(self)
        self.wc.grid(row=3, column=0, columnspan=1)
        self.ip.grid(row=3, column=1, columnspan=1)
        self.op.grid(row=3, column=2, columnspan=1)

        Button(self, text="Get files", command=self.play).grid(row=4, column=0)

    # complete the implementation of play()
    def play(self):
        self.wc = self.wc.get().split(' ')
        Work(int(self.now.get()),int(self.ppw.get()),self.wc,self.ip.get(),self.op.get())
        #Work(int(str(self.now)),int(str(self.ppw)),str(self.wc),str(self.ip),str(self.op))
x = UserInterface().mainloop()