import tkinter as tk
from tkinter import ttk

class ModoEcuacionLineal:
    def __init__(self, parent):
        self.parent = parent

    def ejecutar(self):
        self.parent.geometry("300x200")
        self.parent.title("Modo Ecuación Lineal")

        a_label = ttk.Label(self.parent, text="Ingrese el valor de 'a' (coeficiente de x):")
        a_label.pack()

        a_entry = ttk.Entry(self.parent)
        a_entry.pack()

        b_label = ttk.Label(self.parent, text="Ingrese el valor de 'b' (término independiente):")
        b_label.pack()

        b_entry = ttk.Entry(self.parent)
        b_entry.pack()

        resultado_label = ttk.Label(self.parent, text="Solución:")
        resultado_label.pack()

        resultado_entry = ttk.Entry(self.parent, state='readonly')
        resultado_entry.pack()

        def calcular():
            try:
                a = float(a_entry.get())
                b = float(b_entry.get())
                if a == 0:
                    resultado = "El coeficiente 'a' debe ser diferente de 0."
                else:
                    resultado = -b / a
                resultado_entry.config(state='normal')
                resultado_entry.delete(0, tk.END)
                resultado_entry.insert(0, str(resultado))
                resultado_entry.config(state='readonly')
            except ValueError:
                resultado_entry.config(state='normal')
                resultado_entry.delete(0, tk.END)
                resultado_entry.insert(0, "Error")
                resultado_entry.config(state='readonly')

        calcular_button = ttk.Button(self.parent, text="Calcular", command=calcular)
        calcular_button.pack()

        cerrar_button = ttk.Button(self.parent, text="Cerrar ventana", command=self.parent.destroy)
        cerrar_button.pack()
