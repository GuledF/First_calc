from tkinter import *
import math


z = 0
v = "0+"
cv = 0

root = Tk()
root.title("Calculator!")
root.configure(bg="Dark Grey")
root.geometry("231x410")
root.resizable(width=False, height=False)


screen = Entry(root, width=21, borderwidth=7, state='disabled', font="times")
text1 = Label(root, text="Guleds Calculator!", padx=33, pady=25, bg="black", fg="yellow")


def click(x):
    global z
    global cv
    if cv > 0:
        clearst()
    screen.config(state='normal')
    screen.insert(END, x)
    if len(screen.get()) > 20:
        screen.insert(0, ("Too many characters           "))
    screen.config(state='disabled')


def clearst():
    global cv
    global z
    global v
    screen.config(state='normal')
    screen.delete(0, END)
    z = 0
    v = "0 +"
    cv = 0
    screen.config(state='disabled')


def addition():
    global z
    global v
    screen.config(state='normal')
    math(screen.get() + ")" + "+")
    screen.delete(0, END)
    screen.config(state='disabled')


def subtraction():
    global z
    global v
    screen.config(state='normal')
    math(screen.get() + ")" + "-")
    screen.delete(0, END)
    screen.config(state='disabled')


def multiplication():
    global z
    global v
    screen.config(state='normal')
    math(screen.get() + ")" + "*")
    screen.delete(0, END)
    screen.config(state='disabled')


def division():
    global z
    global v
    screen.config(state='normal')
    math(screen.get() + ")" + "/")
    screen.delete(0, END)
    screen.config(state='disabled')


def math(x):
    global z
    global v
    v = "(" + v + "" + x
    print(v)


def equals():
    global v
    global z
    global cv
    screen.config(state='normal')

    try:
        if z == v:
            v = v
            screen.delete(0, END)
            screen.insert(0, round(eval(v), 3))
        else:
            v = v + screen.get()

            root.clipboard_clear()
            root.clipboard_append(v)
            root.update()

            screen.delete(0, END)
            screen.insert(0, round(eval(v), 3))

    except Exception:
        screen.insert(0, "Enter Calculations Correctly")

    if len(screen.get()) > 20:
        screen.insert(0, ("Error                                                               "))
    z = v
    cv = cv + 1
    screen.config(state='disabled')


b0 = Button(root, text="0", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("0"))
b1 = Button(root, text="1", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("1"))
b2 = Button(root, text="2", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("2"))
b3 = Button(root, text="3", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("3"))
b4 = Button(root, text="4", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("4"))
b5 = Button(root, text="5", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("5"))
b6 = Button(root, text="6", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("6"))
b7 = Button(root, text="7", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("7"))
b8 = Button(root, text="8", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("8"))
b9 = Button(root, text="9", padx=10, pady=10, bg="grey", font="times 20", command=lambda: click("9"))
clear = Button(root, text="Clear", padx=15, pady=10, bg="grey", font="times 20", command=clearst)
dev = Button(root, text="/", padx=13, pady=10, bg="grey", font="times 20", command=division)
add = Button(root, text="+", padx=10, pady=10, bg="grey", font="times 20", command=addition)
less = Button(root, text="-", padx=12, pady=10, bg="grey", font="times 20", command=subtraction)
mul = Button(root, text="*", padx=10, pady=10, bg="grey", font="times 20", command=multiplication)
eq = Button(root, text="=", padx=10, pady=10, bg="grey", font="times 20", command=equals)


b0.grid(row=8, column=0, padx=1, pady=1)
b1.grid(row=7, column=0, padx=1, pady=1)
b2.grid(row=7, column=1, padx=1, pady=1)
b3.grid(row=7, column=2, padx=1, pady=1)
b4.grid(row=6, column=0, padx=1, pady=1)
b5.grid(row=6, column=1, padx=1, pady=1)
b6.grid(row=6, column=2, padx=1, pady=1)
b7.grid(row=5, column=0, padx=1, pady=1)
b8.grid(row=5, column=1, padx=1, pady=1)
b9.grid(row=5, column=2, padx=1, pady=1)
clear.grid(row=8, column=1, padx=1, pady=1, columnspan=2)
dev.grid(row=4, column=3, padx=1, pady=1)
add.grid(row=5, column=3, padx=1, pady=1)
less.grid(row=6, column=3, padx=1, pady=1)
mul.grid(row=7, column=3, padx=1, pady=1)
eq.grid(row=8, column=3, padx=1, pady=1)


screen.grid(row=3, column=0, padx=1, pady=1, columnspan=4)
text1.grid(row=4, column=0, padx=1, pady=1, columnspan=3)

root.mainloop()
