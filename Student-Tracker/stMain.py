from tkinter import *
import tkinter as tk
from tkinter import messagebox



# Be sure to import out other modules
import stGUI
import stFunc


# Frame is the Tkinter frame class that our own class wll inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Width, Height)
        self.master.maxsize(500,300)
        # Call function to center window.
        stFunc.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # User clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: stFunc.ask_quit(self))
        arg = self.master


        # Load in the GUI
        stGUI.load_gui(self)

if __name__ == "__main__":  
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
