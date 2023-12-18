from tkinter import ttk, scrolledtext
import PyPil
import tkinter as tk

def isFloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Crear ventana
frame = tk.Tk()
frame.title("Calculadora de Polinomios y Ecuaciones")
frame.geometry("400x300")
frame.iconbitmap("icon.ico")
frame.configure(bg='lightblue')
frame.resizable(False, False)

# Crear fondo
background = tk.Canvas(frame, width=400, height=300)
background.pack()
backgroundImage = tk.PhotoImage(file='background.png')
background.create_image(0, 0, anchor=tk.NW, image=backgroundImage)

#Entrada de texto
entry = tk.Entry(frame, width=55, borderwidth=1)
entry.place(x = 30, y = 30)

#Salida de texto
label_text = tk.StringVar()
label_text.set("Resultado")
label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
label.place(x=30, y=60)

#Choice box
selected_value = tk.StringVar()
options = ["Ecuación 1r Grado", "Ecuación 2ndo Grado", "Ecuación 3r+ Grado", "Suma de Polinomios", "Resta de Polinomios", "Multiplicación de Polino.", "División de Polinomios", "Extraer las raíces", "Exponenciación de Polin."]
combobox = ttk.Combobox(frame, values=options, textvariable=selected_value, state='readonly')
combobox.place(x = 30, y = 93)
#texto_salida = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=10)
#texto_salida.place(x = 30, y = 93)

def on_enter_pressed(event):
    label_text = tk.StringVar()
    label_text.set("Resultado")
    label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
    label.place(x=30, y=60)
    contenido = entry.get()
    contenidoFinal = []

    if combobox.get() == "Ecuación 1r Grado":
        contenido = contenido.replace(" ", "")
        contenido = contenido.replace("+", "")
        contenido = list(contenido)
        possibleNumerator = 0
        lastWasFloat = False
        for e in contenido:
            doNothing = False
            if e == "(" or e == ")" or e == "=" or e == "/" and not doNothing:
                contenidoFinal.append(e)
                lastWasFloat = False
                doNothing = True
            if isFloat(e) and not doNothing:
                contenidoFinal.append(float(e))
                lastWasFloat = True
                doNothing = True
            if e == "x" and not doNothing:
                if lastWasFloat:
                    contenidoFinal[-1] = str(contenidoFinal[-1]) + "x"
                else:
                    contenidoFinal.append("x")
                lastWasFloat = False
        label_text = tk.StringVar()
        label_text.set(PyPil.EQ1(contenidoFinal))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Ecuación 2ndo Grado":
        contenido = contenido.split()
        contenidoFinal = []
        for e in contenido:
            contenidoFinal.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.EQ2(contenidoFinal))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Ecuación 3r+ Grado":
        contenido = contenido.split()
        contenidoFinal = []
        for e in contenido:
            contenidoFinal.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.EQ3p(contenidoFinal))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Suma de Polinomios":
        contenido = contenido.split()
        contenidoFinal1 = []
        contenidoFinal2 = []
        fase1 = True
        for e in contenido:
            if e == "|":
                fase1 = False
            else:
                if fase1:
                    contenidoFinal1.append(float(e))
                else:
                    contenidoFinal2.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.addition(contenidoFinal1, contenidoFinal2))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Resta de Polinomios":
        contenido = contenido.split()
        contenidoFinal1 = []
        contenidoFinal2 = []
        fase1 = True
        for e in contenido:
            if e == "|":
                fase1 = False
            else:
                if fase1:
                    contenidoFinal1.append(float(e))
                else:
                    contenidoFinal2.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.subtraction(contenidoFinal1, contenidoFinal2))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Multiplicación de Polino.":
        contenido = contenido.split()
        contenidoFinal1 = []
        contenidoFinal2 = []
        fase1 = True
        for e in contenido:
            if e == "|":
                fase1 = False
            else:
                if fase1:
                    contenidoFinal1.append(float(e))
                else:
                    contenidoFinal2.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.multiplication(contenidoFinal1, contenidoFinal2))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "División de Polinomios":
        contenido = contenido.split()
        contenidoFinal1 = []
        contenidoFinal2 = []
        fase1 = True
        for e in contenido:
            if e == "|":
                fase1 = False
            else:
                if fase1:
                    contenidoFinal1.append(float(e))
                else:
                    contenidoFinal2.append(float(e))
        label_text = tk.StringVar()
        label_text.set(str(PyPil.division(contenidoFinal1, contenidoFinal2)[0]) + " " + str(PyPil.division(contenidoFinal1, contenidoFinal2)[1]))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Extraer las raíces":
        contenido = contenido.split()
        contenidoFinal = []
        for e in contenido:
            contenidoFinal.append(float(e))
        label_text = tk.StringVar()
        label_text.set(PyPil.PolyRoot(contenidoFinal))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

    elif combobox.get() == "Exponenciación de Polin.":
        contenido = contenido.split()
        contenidoFinal1 = []
        contenidoFinal2 = []
        fase1 = True
        for e in contenido:
            if e == "|":
                fase1 = False
            else:
                if fase1:
                    contenidoFinal1.append(float(e))
                else:
                    contenidoFinal2.append(float(e))
        label_text = tk.StringVar()
        print(contenidoFinal1, contenidoFinal2)
        contenido1 = []
        contenido2 = []
        for e in contenidoFinal1:
            contenido1.append(int(e))
        for e in contenidoFinal2:
            contenido2.append(int(e))
        label_text.set(str(PyPil.PolyPow(contenido1, contenido2[0])))
        label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
        label.place(x=30, y=60)

entry.bind("<Return>", on_enter_pressed)

#Salida de texto
label_text = tk.StringVar()
label_text.set("Resultado")
label = tk.Label(frame, textvariable=label_text, width=47, borderwidth=2, background="white")
label.place(x=30, y=60)

frame.mainloop()