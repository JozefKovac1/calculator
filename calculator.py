from tkinter import *
from math import *

root= Tk()
global num
global math
root.title("Kalkulacka")
e = Entry(root, width= 30, borderwidth= 10)
e.grid(row = 0, column = 0, columnspan= 3)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_scitanie():
    number = e.get()
    global num
    global math
    math = "scitanie"
    num = int(number)
    e.delete(0, END)

def button_odcitanie():
    number = e.get()
    global num
    global math
    math = "odcitanie"
    num = int(number)
    e.delete(0, END)
def button_nasobenie():
    number = e.get()
    global num
    global math
    math = "nasobenie"
    num = int(number)
    e.delete(0, END)

def button_delenie():
    number = e.get()
    global num
    global math
    math = "delenie"
    num = int(number)
    e.delete(0, END)

def button_mocnina():
    number = e.get()
    global num
    global math
    math = "mocnina"
    num = int(number)
    e.delete(0, END)

def button_odmocnina():
    number = e.get()
    global num
    global math
    math = "odmocnina"
    num = int(number)
    e.delete(0, END)

def button_vysledok():
    number = e.get()
    e.delete(0,END)
    global num
    global math

    if math == "scitanie":
        e.insert(0,num + int(number))
    if math == "odcitanie":
        e.insert(0, num - int(number))
    if math == "nasobenie":
        e.insert(0, num * int(number))
    if math == "delenie":
        e.insert(0,num / int(number))
    if math == "mocnina":
        e.insert(0,pow((int(number)),2))
    if math == "odmocnina":
        e.insert(0, sqrt(int(number)))

def button_clear():
    e.delete(0,END)

#cisla na kalkulacke
button_1 = Button(root, text = "1",padx=40,pady = 20, command= lambda: button_click(1))
button_2 = Button(root, text = "2", padx=40,pady = 20,command= lambda: button_click(2))
button_3 = Button(root, text = "3", padx=40,pady = 20,command= lambda: button_click(3))
button_4 = Button(root, text = "4", padx=40,pady = 20,command= lambda: button_click(4))
button_5 = Button(root, text = "5", padx=40,pady = 20,command= lambda: button_click(5))
button_6 = Button(root, text = "6", padx=40,pady = 20,command= lambda: button_click(6))
button_7 = Button(root, text = "7", padx=40,pady = 20,command= lambda: button_click(7))
button_8 = Button(root, text = "8", padx=40,pady = 20,command= lambda: button_click(8))
button_9 = Button(root, text = "9", padx=40,pady = 20,command= lambda: button_click(9))
button_0 = Button(root, text = "0", padx=40,pady = 20,command= lambda: button_click(0))
#znak scitania, odcitania, nasobenia, delenia, mocnica, odmocnina, clear

button_clear = Button(root, text= "Clear",padx=40,pady = 20, command= button_clear)
button_scitanie = Button(root, text = "+",padx=40,pady = 20, command=button_scitanie)
button_odcitanie = Button(root, text = "-",padx=40,pady = 20, command = button_odcitanie)
button_nasobenie = Button(root, text = "*",padx=40,pady = 20, command= button_nasobenie)
button_delenie = Button(root,text = "/",padx=40,pady = 20, command = button_delenie)
button_mocnica = Button(root, text = "Sqr",padx=40,pady = 20, command= button_mocnina)
button_odmocnina = Button(root,text = "Sqrt",padx=40,pady = 20, command = button_odmocnina)
button_vysledok = Button(root,text = "=",padx=91,pady = 20, command=button_vysledok,fg = "black", bg = "light blue")


#vyzobrazenie vsetkeho na tk

button_7.grid(row = 1, column=0)
button_8.grid(row = 1, column=1)
button_9.grid(row = 1, column=2)

button_4.grid(row = 2, column=0)
button_5.grid(row = 2, column=1)
button_6.grid(row = 2, column=2)

button_1.grid(row = 3, column=0)
button_2.grid(row = 3, column=1)
button_3.grid(row = 3, column=2)

button_0.grid(row = 4, column=1)
button_mocnica.grid(row =4,column=0)
button_odmocnina.grid(row = 4, column=2)

button_nasobenie.grid(row = 2, column=3)
button_delenie.grid(row = 1, column= 3)
button_scitanie.grid(row = 3, column= 3)
button_odcitanie.grid(row = 4, column=3)

button_vysledok.grid(row =5,column=0, columnspan=3)
button_clear.grid(row = 5, column =3)

root.mainloop()