

import os
from tkinter import *
import tkinter as tk
import sqlite3

# Be sure to import our other modules
# so we can have access to them
import student_main
import student_gui


def center_window(self, w, h): # pass in the tkinter frame (master) refeerence and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to pain the app cenetered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)






#=================================================================


def create_db(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT,\
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT\
            );")
        # You must commit() to save changes and close the database connection
        conn.commit()
    conn.close()
    first_run(self)



def first_run(self):
    data = ('Chris', 'Sexton', 'Chris Sexton', '819-683-3217', 'chris@school.com', 'Python')
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student(col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_student""")
    count = cur.fetchone()[0]
    return cur,count


# Select item in ListBox
def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_student WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # this returns a tuple and we can slice it into 4 parts using data[] during iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])




        def addToList(self):
            var_fname = self.txt_fname.get()
            var_lname = self.txt_lname.get()
            # normalize the data to keep it consistent in the database
            var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
            var_lname = var_lname.strip() # This will ensure that the first character in each wordd in capitalized
            var_fname = var_fname.title()
            var_lname = var_lname.title()
            var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normialized names into a fullname
            print("var_fullname: {}".format(var_fullname)) # just shows for me
            var_phone = self.txt_phone.get().strip()
            var_email = self.txt_email.get().strip()
            var_course = self.txt_course.get().strip()
            if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
                conn = sqlite3.connect('student')
                with conn:
                    cursor = conn.cursor()
                    # Check the database for the existance of the fullname, if so we will alert user and disregard request
                    cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student WHERE col_fullname = '{}'""".format(var_fullname))
                    count = cursor.fetchone()[0]
                    chkName = count
                    if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                        print("chkName: {}".format(chkname))
                        cursor.execute("""INSERT INTO tbl_student(col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""")
                        self.lst.List1.insert(END,var_fullname) # update listbox with new fullname
                        onClear(self) # call the function to clear all of the textboxes
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Missing Text Error","Please ensure that there is data in all five fields.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite.connect('student.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cur.fethcone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select()))
            if confirm:
                conn = sqlite3.connect("student.db")
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textbooks and the selected index of the listbox
####                onRefresh(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select))
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
##      onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)


def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be allowed to update changes for phone, email and course
    # For name changes, the user wil need to delete the entire record and start over.
    var_phone = self.txt_phone().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email().strip()
    var_course = self.txt_course().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0): # ensure that there is data present
        conn = sqlite3.connect('student.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_student WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fethcone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_student WHERE col_email = '{}'""".format(var_email))
            count = cur.fethcone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(col_course) FROM tbl_student WHERE col_course = '{}'""".format(var_course))
            count = cur.fethcone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) and ({}) will be implemented for ({}). \nProceed with the update request?".format(var_phone,var_email,var_course))
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_student SET col_phone = '{0}',col_email = '{1}',col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update has been cancelled.".format(var_phone,var_email,var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, email course information.")
    onClear(self)
                
    
            
            
if __name__ == "__main__":
    pass
