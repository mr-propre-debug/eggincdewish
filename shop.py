import tkinter as tk
from tkinter import messagebox

from data import Data

class Shop:

    def __init__(self, width, height):
        dataObj = Data
        data = dataObj.getData()
        self.width = width
        self.height = height
        self.root = tk.Tk()

        canvas1 = tk.Canvas(self.root, width=width, height=height, relief='raised')
        canvas1.pack()

        eggs = tk.StringVar()
        eggs.set(f'money : {dataObj.getData()["money"]}')

        showEggs = tk.Label(self.root, textvariable=eggs)
        showEggs.config(font=('assets/font.ttf', 14))
        canvas1.create_window(200, 25, window=showEggs)

        def upgrade_1():
            if data["money"] >= 500:
                data["money"] -= 500
                data["eggLayingRate"] += 0.1
                data["money"] = round(data["money"], 2)
                data["eggLayingRate"] = round(data["eggLayingRate"], 2)
                dataObj.save(data)
                eggs.set(f'money : {dataObj.getData()["money"]}')
                self.root.update_idletasks()
            else:
                messagebox.showerror("Upgarde ERROR", "You don't have enough money to buy that upgrade !")
            
        upgrade1 = tk.Button(text='upgrade 1', command=upgrade_1, bg='brown', fg='white', font=('assets/font.ttf', 9, 'bold'))
        canvas1.create_window(200, 180, window=upgrade1)

        close = tk.Button(text='close shop', command=self.root.destroy, bg='brown', fg='white', font=('assets/font.ttf', 9, 'bold'))
        canvas1.create_window(200, 220, window=close)

        self.root.mainloop()