import tkinter as tk

def on_button_click(number):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(number))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Simple")

# Crear una entrada para mostrar los números
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Crear los botones del 0 al 9
for i in range(10):
    if i == 0:
        button = tk.Button(root, text=str(i), padx=20, pady=10, command=lambda i=i: on_button_click(i))
    else:
        button = tk.Button(root, text=str(i), padx=20, pady=10, command=lambda i=i: on_button_click(i))
    row_val = (9 - i) // 3 + 1
    col_val = (9 - i) % 3
    button.grid(row=row_val, column=col_val)

# Iniciar el bucle de eventos de Tkinter
root.mainloop()