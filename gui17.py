from tkinter import *


root = Tk()
root.geometry('644x456')
root.title('GUI Work page')
root.wm_iconbitmap("images/1.ico")
root.configure(background='Purple')

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width},{height}")

Button(root, text='Close', command=root.destroy).pack()
root.mainloop()