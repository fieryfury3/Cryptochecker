import tkinter as tk

window = tk.Tk()

window.title("CoinMarketCap")

window.geometry("400x400")

# Functions

# Label
title = tk.Label(text="Please type name of coin: ")title.grid(row=0, column=0)

# Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=0)

# Button
button1 = tk.Button(text="Search")
button1.grid(column=1, row=1)

# Text Field
text_field = tk.Text(master=window, height=10, width=20)
text_field.grid()

window.mainloop()

