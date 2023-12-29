import tkinter as tk
from tkinter import messagebox

from data import Data

class GameSettings:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.root= tk.Tk()

        canvas1 = tk.Canvas(self.root, width=width, height=height, relief='raised')
        canvas1.pack()

        label1 = tk.Label(self.root, text='Save')
        label1.config(font=('assets/font.ttf', 14))
        canvas1.create_window(200, 25, window=label1)

        def manualSave():
            dataObj = Data
            data = dataObj.getData()
            dataObj.manualSave(data)
            self.root.destroy()

        button1 = tk.Button(text='save', command=manualSave, bg='brown', fg='white', font=('assets/font.ttf', 9, 'bold'))
        canvas1.create_window(200, 50, window=button1)

        self.root.mainloop()