from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import  random
import  time
import  datetime

def main():
    root = Tk()
    app = Window1(root)
class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Pharmacy System')
        self.master.geometry('1350x750')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.LabelTitle = Label(self.frame,text='Pharmacy Management System',font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=20)
        self.LoginFrame1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1010, height=200, bd=20, relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)
        self.LoginFrame3 = Frame(self.frame, width=1010, height=100, bd=20, relief='ridge')
        self.LoginFrame3.grid(row=3, column=0, pady=2)

        # self.btnRegistration = Button(self.LoginFrame3, text='Patient Registration System', command=self.Registration_window)
        # self.btnRegistration.grid(row=0, column=0)
        # self.btnHospital = Button(self.LoginFrame3, text='Hospital Management System', bg='blue', command=self.Hospital_window)
        # self.btnHospital.grid(row=0, column=1)

        self.btnLogin = Button(self.LoginFrame2, text='Login', width=20, font=SUNKEN, command=self.Registration_window)
        self.btnLogin.grid(row=0, column=0)
        self.btnReset = Button(self.LoginFrame2, text='Reset', width=20, font=SUNKEN, bg='blue', command=self.Hospital_window)
        self.btnReset.grid(row=0, column=1)
        self.btnExit = Button(self.LoginFrame2, text='Exit', width=20, font=SUNKEN, bg='blue', command=self.Hospital_window)
        self.btnExit.grid(row=0, column=2)

        self.btnRegistration = Button(self.LoginFrame3, text='Patient Registration System', command=self.Registration_window)
        self.btnRegistration.grid(row=0, column=0)
        self.btnHospital = Button(self.LoginFrame3, text='Hospital Management System', bg='blue', command=self.Hospital_window)
        self.btnHospital.grid(row=0, column=1)
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title('Patient Registration System')
        self.master.geometry('1350x750')
        self.frame = Frame(self.master)
        self.frame.pack()

class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('1350x750')
        self.frame = Frame(self.master)
        self.frame.pack()

main()