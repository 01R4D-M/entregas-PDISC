from tkinter import Tk, Label, Button, Entry
ventana = Tk()
ventana.title("Ejemplo con place")
ventana.geometry("400x200")
def sumar():
    n1 = int(txt1.get())
    n2 = int(txt2.get())

    r = n1 + n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

lbl1 = Label(ventana, text="Primer numero", bg="yellow")
lbl1.place(relx=0.05, rely=0.07)

lbl2 = Label(ventana, text="Segundo numero", bg="yellow")
lbl2.place(relx=0.05, rely=0.32)

lbl3 = Label(ventana, text="Resultado", bg="yellow")
lbl3.place(relx=0.05, rely=0.62)

txt1 = Entry(ventana, text="Primer numero", bg="orange")
txt1.place(relx=0.35, rely=0.07)

txt2 = Entry(ventana, text="Segundo numero", bg="orange")
txt2.place(relx=0.35, rely=0.32)

txt3 = Entry(ventana, text="Resultado", bg="orange")
txt3.place(relx=0.35, rely=0.62)

btn1 = Button(ventana, text="SUMA", bg="pink", command=sumar)
btn1.place(relx=0.05, rely=0.62)

ventana.mainloop()