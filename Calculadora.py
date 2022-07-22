from tkinter import *
root = Tk()
root.title('Calculadora Científica')
miframe = Frame(root)
miframe.pack(fill="both", expand=True)
#estiramiento
for i in range(1,5):
    Grid.columnconfigure(miframe, i, weight=1)
for i in range(1,8):
    Grid.rowconfigure(miframe, i, weight=1)

operacion=""
resultado=0
resultadomult=1


#--------------pantalla-----------------------------------------------
digito = StringVar()
digito.set("0")
pantalla = Entry(miframe, textvariable=digito)
pantalla.grid(row=1, column=1, columnspan=4, sticky="NSEW")
pantalla.config(fg="white", bg="black", font=("SemiBold",24), justify="right")

#-------------funciones----------------------------------------------------------------
contsuma=0
contmult=0
contres=0
contdiv=0
continversa=0
def suma(num):
    global operacion, resultado, contsuma
    operacion="suma"
    resultado+=float(num)
    digito.set(resultado)
    contsuma=1

def multiplicacion(num):
    global operacion,resultadomult, contmult
    operacion="mult"
    resultadomult=resultadomult*float(num)
    digito.set(resultadomult)
    contmult=1

def resta(num):
    global operacion, resultado, contres
    if contres==0:
        resultado=float(num)
    else:
        resultado-=float(num)
    operacion="resta"
    digito.set(resultado)
    contres=1

def division(num):
    global operacion, resultadomult, contdiv
    operacion="div"
    if contdiv==0:
        resultadomult=float(num)
    else:
        try:
            resultadomult=resultadomult/float(digito.get())
            digito.set(resultadomult)
        except ZeroDivisionError:
            digito.set("¿Vos sos estúpido?")
    contdiv=1

def inversa(num):
    global operacion, resultadomult, continversa
    operacion="inv"
    if float(num)!=0:
        resultadomult=1/float(num)
        digito.set(resultadomult)
    else:
        digito.set("¿Sos pelotudo?")

def igual():
    global contsuma, contmult, contres,contdiv, resultado, resultadomult
    if contsuma==1:
        digito.set(resultado+float(digito.get()))
        resultado=0
        contsuma=0
    elif contmult==1:
        digito.set(resultadomult*float(digito.get()))
        resultadomult=1
        contmult=0
    elif contres==1:
        digito.set(resultado-float(digito.get()))
        resultado=0
        contres=0
    elif contdiv==1:
        try:
            resultadomult=resultadomult/float(digito.get())
            digito.set(resultadomult)
        except ZeroDivisionError:
            digito.set("¿Vos sos estúpido?")
        resultadomult=1
        contdiv=0

def borrar():
    digito.set(digito.get()[:-1])

def C():
    resultado=0
    resuladomult=1
    digito.set("0")

def CE():
    digito.set("0")
#---------------pulsaciones--------------------------------------------
def numeropantalla(num):
    global operacion, subpan
    if operacion != "":
        digito.set(num)
        operacion = ""
    else:
        if digito.get() == "0" and num == "0":
            digito.set("0")
        elif digito.get() == "0" and num == ".":
            digito.set("0.")
        elif digito.get() == "0" and num != "0":
            digito.set(num)

        else:
            if digito.get().count(".") == 0:
                digito.set(digito.get() + num)
            elif digito.get().count(".") >= 1 and num == ".":
                digito.get()
            else:
                digito.set(digito.get() + num)


#---------------botones-----------------------

#fila 1
botonporcentaje=Button(miframe, text="%", width=5, font='Semibold').grid(row=2, column=1, sticky="NSEW")
botonce=Button(miframe, text="CE", width=5, font='Semibold', command=lambda:CE()).grid(row=2, column=2, sticky="NSEW")
botonc=Button(miframe, text="C", width=5, font='Semibold', command=lambda:C()).grid(row=2, column=3, sticky="NSEW")
botonborrar=Button(miframe, text="DEL", width=5, font='Semibold', command=lambda:borrar()).grid(row=2, column=4, sticky="NSEW")
#fila 2
botoninversa=Button(miframe, text="1/x", width=5, font='Semibold', command=lambda:inversa(digito.get())).grid(row=3, column=1, sticky="NSEW")
botoncuadrado=Button(miframe, text="x^2", width=5, font='Semibold').grid(row=3, column=2, sticky="NSEW")
botonraiz=Button(miframe, text="x^(1/2)", width=5, font='Semibold').grid(row=3, column=3, sticky="NSEW")
botondividir=Button(miframe, text="/", width=5, font='Semibold', command=lambda:division(digito.get())).grid(row=3, column=4, sticky="NSEW")
#fila 3
boton7=Button(miframe, text="7", width=5, font='Semibold', command=lambda:numeropantalla('7')).grid(row=4, column=1, sticky="NSEW")
boton8=Button(miframe, text="8", width=5, font='Semibold', command=lambda:numeropantalla("8")).grid(row=4, column=2, sticky="NSEW")
boton9=Button(miframe, text="9", width=5, font='Semibold', command=lambda:numeropantalla("9")).grid(row=4, column=3, sticky="NSEW")
botonmultiplicar=Button(miframe, text="X", width=5, font='Semibold',command=lambda:multiplicacion(digito.get())).grid(row=4, column=4, sticky="NSEW")
#fila 4
boton4=Button(miframe, text="4", width=5, font='Semibold', command=lambda:numeropantalla("4")).grid(row=5, column=1, sticky="NSEW")
boton5=Button(miframe, text="5", width=5, font='Semibold', command=lambda:numeropantalla("5")).grid(row=5, column=2, sticky="NSEW")
boton6=Button(miframe, text="6", width=5, font='Semibold', command=lambda:numeropantalla("6")).grid(row=5, column=3, sticky="NSEW")
botonresta=Button(miframe, text="-", width=5, font='Semibold', command=lambda:resta(digito.get())).grid(row=5, column=4, sticky="NSEW")
#fila 5
boton1=Button(miframe, text="1", width=5, font='Semibold', command=lambda:numeropantalla("1")).grid(row=6, column=1, sticky="NSEW")
boton2=Button(miframe, text="2", width=5, font='Semibold', command=lambda:numeropantalla("2")).grid(row=6, column=2, sticky="NSEW")
boton3=Button(miframe, text="3", width=5, font='Semibold', command=lambda:numeropantalla("3")).grid(row=6, column=3, sticky="NSEW")
botonsuma=Button(miframe, text="+", width=5, font='Semibold', command=lambda:suma(digito.get())).grid(row=6, column=4, sticky="NSEW")
#fila 6
botoncoma=Button(miframe, text=",", width=5, font='Semibold', command=lambda:numeropantalla(".")).grid(row=7, column=1, sticky="NSEW")
boton0=Button(miframe, text="0", width=5, font='Semibold', command=lambda:numeropantalla("0")).grid(row=7, column=2, sticky="NSEW")
botonigual=Button(miframe, text="=", width=5, font='Semibold', command=lambda:igual()).grid(row=7, column=3, columnspan=4, sticky="NSEW")

root.mainloop()