from tkinter import *

ventana = Tk()
ventana.title("Operaciones")

def suma():
    result = 0
    num1 = n1.get()
    num2 = n2.get()
    result = int(num1 + num2)
    resultado.delete(0, END)
    resultado.insert(0, result)

def resta():
    result = 0
    num1 = n1.get()
    num2 = n2.get()
    result = num1 - num2
    resultado.delete(0, END)
    resultado.insert(0, result)

def mult():
    result = 0
    num1 = n1.get()
    num2 = n2.get()
    result = num1 * num2
    resultado.delete(0, END)
    resultado.insert(0, result)

def div():
    result = 0
    num1 = n1.get()
    num2 = n2.get()
    result = num1 / num2
    resultado.delete(0, END)
    resultado.insert(0, result)

def exponencial():
    result = 0
    num1 = n1.get()
    num2 = n2.get()
    result = 1
    result = num1 ** num2
    resultado.delete(0, END)
    resultado.insert(0, result)

def borrar():
    input1.delete(0, END)
    input2.delete(0, END)
    resultado.delete(0, END)

def salir():
    ventana.destroy()

ventana.geometry("500x200")

n1 = IntVar()
n2 = IntVar()

Label(ventana, text="Num 1").place(x=20, y=20)
input1 = Entry(ventana, textvariable=n1)
input1.place(x=70, y=20)
Label(ventana, text="Num 2").place(x=20, y=50)
input2 = Entry(ventana, textvariable=n2)
input2.place(x=70, y=50)
Label(ventana, text="Resultado:").place(x=250, y=30)
resultado = Entry(ventana)
resultado.place(x=320, y=30)
Button(ventana, text="  +  ", command=suma).place(x=140, y=80)
Button(ventana, text="  -  ", command=resta).place(x=180, y=80)
Button(ventana, text="  *  ", command=mult).place(x=220, y=80)
Button(ventana, text="  /  ", command=div).place(x=260, y=80)
Button(ventana, text="  ^  ", command=exponencial).place(x=300, y=80)
Button(ventana, text=" Borrar ", command=borrar).place(x=180, y=110)
Button(ventana, text=" Salir ", command=salir).place(x=230, y=110)

ventana.mainloop()