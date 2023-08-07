import tkinter as tk
from tkinter import ttk

class ModoPolinomios:
    def __init__(self, parent):
        self.parent = parent

    def ejecutar(self):
        self.parent.geometry("400x300")
        self.parent.title("Modo Polinomios")

        grado_label = ttk.Label(self.parent, text="Ingrese el grado del polinomio:")
        grado_label.pack()

        grado_entry = ttk.Entry(self.parent)
        grado_entry.pack()

        coeficientes_label = ttk.Label(self.parent, text="Ingrese los coeficientes:")
        coeficientes_label.pack()

        coeficientes_entries = []

        def create_coeficientes_entries():
            for entry in coeficientes_entries:
                entry.destroy()
            coeficientes_entries.clear()

            grado = int(grado_entry.get())
            for i in range(grado, -1, -1):
                coef_label = ttk.Label(self.parent, text=f"Coeficiente para x^{i}:")
                coef_label.pack()
                coef_entry = ttk.Entry(self.parent)
                coef_entry.pack()
                coeficientes_entries.append(coef_entry)

        grado_entry.bind('<Return>', lambda event: create_coeficientes_entries())

        resultado_label = ttk.Label(self.parent, text="Resultado:")
        resultado_label.pack()

        resultado_entry = ttk.Entry(self.parent, state='readonly')
        resultado_entry.pack()

        def calcular():
            try:
                grado = int(grado_entry.get())
                coeficientes = [float(entry.get()) for entry in coeficientes_entries]
                x = float(x_entry.get())
                resultado = sum(coef * (x ** i) for i, coef in enumerate(coeficientes))
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

        x_label = ttk.Label(self.parent, text="Ingrese el valor de 'x' para evaluar el polinomio:")
        x_label.pack()

        x_entry = ttk.Entry(self.parent)
        x_entry.pack()
