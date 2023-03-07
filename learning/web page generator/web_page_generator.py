#
# Python Ver:       3.10.7
#
# Author:           Bryan
#
# Purpose:          Web Page Generator assignment.
#                   
# Tested OS:        This code was written and tested to work with Windows 11.

import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # label
        customLabel= Label(self.master, text= "Enter custom text or click the Default HTML page button")
        customLabel.grid(row=0, column=0, padx=(20,5) , pady=(10,10))

        # entry box
        self.customText = Entry(self.master, bd =5, width=125)
        self.customText.grid(row=1, column=0, columnspan=3)        

        # Creates a button to generate a Custome page.
        self.btn = Button(self.master, text="Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))        
                  
        # Creates a button to generate a HTML page.
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))  

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")        


    # code for html file
    def customHTML(self):
        # custom html file
        htmlText = self.customText.get()
        customFile = open("index.html", "w")
        customContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")    

    




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
