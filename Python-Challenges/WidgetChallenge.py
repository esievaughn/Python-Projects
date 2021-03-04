
import tkinter
from tkinter import *
from tkinter import filedialog
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.Browse = StringVar()
        self.Browse1 = StringVar()

        #Button formatting 
        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1,  command=self.askdirectory)
        self.btnBrowse.grid(row=0, column=0, padx=20,pady=(50,10))

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1,  command=self.askdirectory)
        self.btnBrowse1.grid(row=1, column=0, padx=20,pady=10)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row=2, column=0, padx=20,pady=10)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btnClose.grid(row=2, column=1, sticky=E)      

        #Input formatting
        self.txt1 = Entry(self.master, text=self.Browse, width=50,)
        self.txt1.grid(row=0, column=1, padx=10, pady=(50,10), sticky=E)

        self.txt2 = Entry(self.master, text=self.Browse1, width=50,)
        self.txt2.grid(row=1, column=1, padx=10, pady=10, sticky=E)

    def close(self):
        self.master.destroy()

    
    def askdirectory(self):
        dirname = filedialog.askdirectory()
        self.Browse.set(dirname)




       


if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
