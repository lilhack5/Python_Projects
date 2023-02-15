#
# Python Ver:       3.10.7
#
# Author:           Bryan
#
# Purpose:          Student tracking assignment.
#                   
# Tested OS:        This code was written and tested to work with Windows 11.

from tkinter import *
import tkinter as tk

# Be sure to import the other mudules
# so we can have access to them
import student_gui
import student_func

# Frame is the Tkinter frame class the our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

            # define our master frame configuration
        self.master = master
        self.master.minsize(555,355) #(height, width)
        self.master.maxsize(555,355)
        # This CenterWindow method will center our app on the user's screen
        student_func.center_window(self,555,355)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        # keeping your code comparmentalized and clutter free
        student_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
