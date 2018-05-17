from tkinter import *

blank_window = Tk()

labelone = Label(blank_window, text="Name")
labeltwo = Label(blank_window, text="Password")
entry_1 = Entry(blank_window)
entry_2 = Entry(blank_window)


labelone.grid(row=0, sticky=E)
labeltwo.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox = Checkbutton(blank_window, text="Keep me logged in")
checkbox.grid(columnspan=2)

blank_window.mainloop()