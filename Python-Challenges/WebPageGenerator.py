import webbrowser
from tkinter import *
from tkinter import filedialog
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,200))
        self.master.title("Web Page Generator")
        self.master.config(bg='lightgray')
                             
        #label
        self.lblMain = Label(self.master,bg='lightgray',text='INPUT HTML BODY UPDATE BELOW:')
        self.lblMain.grid(row=0,column=0,padx=15,pady=15, sticky=N+S+E+W)

        #text box
        self.txtBox = tk.Entry(self.master,width=70,text='')
        self.txtBox.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        
        #buttons
        self.btnUpdate = tk.Button(self.master,width=12,height=2,text='Update Website', command=lambda: update(self))
        self.btnUpdate.grid(row=2,column=0,padx=20,pady=10,sticky=SW)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btnClose.grid(row=2, column=0, sticky=E)  

        #functions
        def update(self):
             hardcode =""" <html>
                                <body>
                                    <h1>
                                        Stay tuned for our amazing summer sale!
                                    </h1>
                        """
             updateBody = self.txtBox.get()
             hardcode2="""
                                </body>
                            </html>
                        """
             with open("basic.html", "w") as file:
                 file.write(hardcode + updateBody + hardcode2)
                
             webbrowser.open_new_tab("basic.html")

    def close(self):
        self.master.destroy()





if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

