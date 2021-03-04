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
                             
        #labels
        self.lbl_main = Label(self.master,bg='lightgray',text='INPUT HTML BODY UPDATE BELOW:')
        self.lbl_main.grid(row=0,column=0,padx=15,pady=15, sticky=N+S+E+W)

        #text box
        self.txt_box1 = tk.Entry(self.master,width=70,text='')
        self.txt_box1.grid(row=1, column=0, padx=15, pady=5, sticky=W)
        
        #buttons
        self.btn_update = tk.Button(self.master,width=12,height=2,text='Update Website', command=lambda: update(self))
        self.btn_update.grid(row=2,column=0,padx=20,pady=10,sticky=SW)

        self.btn_close = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btn_close.grid(row=2, column=0, sticky=E)  

        #functions

        
        def update(self):
             hardcode =""" <html>
                                <body>
                                    <h1>
                                        Stay tuned for our amazing summer sale!
                                    </h1>
                        """
             updatebody = self.txt_box1.get()
             hardcode2="""
                                </body>
                            </html>
                        """
             with open("basic.html", "w") as file:
                 file.write(hardcode + updatebody + hardcode2)
                
             webbrowser.open_new_tab("basic.html")

    def close(self):
        self.master.destroy()





if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

