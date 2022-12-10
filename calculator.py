from tkinter import *

root = Tk()

e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.insert(0, '0')


def button_click(number):
    if e.get() == '0':
        e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def button_clear():
    e.delete(0, END)


button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7)).grid(row=2, column=0)
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8)).grid(row=2, column=1)
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9)).grid(row=2, column=2)

button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4)).grid(row=3, column=0)
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5)).grid(row=3, column=1)
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6)).grid(row=3, column=2)

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1)).grid(row=4, column=0)
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=1)
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=2)

button_AC = Button(root, text='AC', padx=35, pady=20, command=lambda: button_clear()).grid(row=5, column=0)
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0)).grid(row=5, column=1)
button_point = Button(root, text='.', padx=41.5, pady=20).grid(row=5, column=2)

button_multiply = Button(root, text='x', padx=40, pady=20).grid(row=2, column=3)
button_subtract = Button(root, text='-', padx=40, pady=20).grid(row=3, column=3)
button_add = Button(root, text='+', padx=38, pady=20).grid(row=4, column=3)
button_equals = Button(root, text='=', padx=38, pady=20).grid(row=5, column=3)

root.mainloop()
