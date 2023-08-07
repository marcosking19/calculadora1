import tkinter as tk
from tkinter import ttk

class ModoNormal:
    def __init__(self, parent):
        self.parent = parent

    def ejecutar(self):
        self.parent.geometry("300x300")
        self.parent.title("Modo Normal")

        input_label = ttk.Label(self.parent, text="Ingrese la operación:")
        input_label.pack()

        input_entry = ttk.Entry(self.parent)
        input_entry.pack()

        resultado_label = ttk.Label(self.parent, text="Resultado:")
        resultado_label.pack()

        resultado_entry = ttk.Entry(self.parent, state='readonly')
        resultado_entry.pack()

        def calcular():
            try:
                operacion = input_entry.get()
                resultado = eval(operacion)
                resultado_entry.config(state='normal')
                resultado_entry.delete(0, tk.END)
                resultado_entry.insert(0, str(resultado))
                resultado_entry.config(state='readonly')
            except Exception as e:
                resultado_entry.config(state='normal')
                resultado_entry.delete(0, tk.END)
                resultado_entry.insert(0, "Error")
                resultado_entry.config(state='readonly')

        calcular_button = ttk.Button(self.parent, text="Calcular", command=calcular)
        calcular_button.pack()

        cerrar_button = ttk.Button(self.parent, text="Cerrar ventana", command=self.parent.destroy)
        cerrar_button.pack()
