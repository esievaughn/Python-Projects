#   FILE TRANSFER CHALLENGE
import os
import datetime as dt
from os import scandir
import shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


#   FRAME IMPORTED FROM TKINTER
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title("CHECK FILES")
        self.master.protocol("EXIT", lambda: askExit(self))        #ASK USER IF THEY WISH TO EXIT
       

        # TEXT BOX FORMATING
        self.txtbox1 = tk.Entry(self.master,width=50,text='')
        self.txtbox1.grid(row=0, column=1, padx=(10, 25), pady=(46, 0),sticky=N+E+W)
        self.txtbox2 = tk.Entry(self.master,text='')
        self.txtbox2.grid(row=1, column=1, padx=(10, 25), pady=(10, 0),sticky=N+E+W)

        # BUTTON FORMATTING
        self.btn_browse1 = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: getSrc(self))
        self.btn_browse1.grid(row=0, column = 0, padx=(15, 25), pady=(45, 10),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: getDst(self))
        self.btn_browse2.grid(row=1, column = 0, padx=(15, 25), pady=(10, 10),sticky=W)
        self.btn_checkFiles = tk.Button(self.master,width=12, height=2,text='COPY FILES',command=lambda: copyFile())
        self.btn_checkFiles.grid(row=2, column = 0, padx=(15,25), pady=(5, 20),sticky=E)
        self.btn_close = tk.Button(self.master,width=12, height=2,text='CLOSE',command=lambda: askExit(self))
        self.btn_close.grid(row=2, column = 1, padx=(0,25), pady=(5, 20),sticky=E)

#   PULL DIRECTORY THAT USER WANTS TO CHECK
def getSrc(self):
    dirname = filedialog.askdirectory()
    self.txtbox1.insert(0,dirname)
    

#   PULL DIRECTOY USER WANTS TO COPY FILES INTO
def getDst(self):
    dirname = filedialog.askdirectory()
    self.txtbox2.insert(0,dirname)


#   ASK TO EXIT PROGRAM
def askExit(self):
    if messagebox.askokcancel("EXIT PROGRAM", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


#   CREATE A FUNCTION UTILIZING WALK METHOD & SHUTIL COPY METHOD (COPIED fROM FileTransfer2.py)
now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = '/Users/Owner/Desktop/NewModified/'
dest = '/Users/Owner/Desktop/HomeOffice/'

def copyFile():
    for root, dirs, files in os.walk(created):
        for fname in files:
            path = os.path.join(root, fname)    #   JOIN FILE SYSTEM PATH WITH FILE NAME
            st = os.stat(path)                  #   RETURN STAT INFO REGARDING SPECIFIED PATH
            mtime = dt.datetime.fromtimestamp(st.st_mtime)  #   MODIFIED TIME
            if mtime > ago:                     #   IF MODIFED IN THE LAST 24 HOURS
                print("CONFIRMED NEW OR EDITED FILED COPIED:  ", fname, " LAST MODIFIED: ", mtime.strftime("%H:%M %m/%d/%Y"))
                shutil.copy(path, dest) 




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
                
