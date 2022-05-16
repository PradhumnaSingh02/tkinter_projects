# Calculator GUI
from tkinter import *

def click(event):
    global strvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if strvalue.get().isdigit():
            value = int(strvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        strvalue.set(value)
        screen.update()
    elif text == "C":
        strvalue.set("")
        screen.update()
    else:
        strvalue.set(strvalue.get() + text)
        screen.update()

root = Tk()
root.geometry('642x900')
root.title('Calculator')
root.wm_iconbitmap("images/1.ico")
strvalue = StringVar()
strvalue = set("")
screen = Entry(root, textvar=strvalue, font='Lucida 40 bold')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg='grey')

b = Button(f, text='9', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='8', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='7', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)

f.pack()
f = Frame(root, bg='grey')
b = Button(f, text='6', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='5', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='4', padx=18, pady=22, font='lucida 35 bold')
b.bind('<Button-1>', click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()
f = Frame(root, bg='grey')
b = Button(f, text='3', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='2', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='1', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg='grey')
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='0', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='+', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='-', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()
f = Frame(root, bg='grey')
b = Button(f, text='*', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='/', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text='C', padx=18, pady=22, font='lucida 35 bold')
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

root.mainloop()