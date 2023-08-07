import tkinter as tk
from tkinter import ttk
from modo_normal import ModoNormal
from modo_complejo import ModoComplejo
from modo_ecuacion_lineal import ModoEcuacionLineal
from modo_polinomios import ModoPolinomios

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()

    def ejecutar_calculadora(self):
        self.root.title("Calculadora")
        self.root.geometry("3000x2000")

        def modo_normal():
            self.root.withdraw()
            subwindow = tk.Toplevel(self.root)
            ModoNormal(subwindow).ejecutar()
            subwindow.protocol("WM_DELETE_WINDOW", lambda: self.root.deiconify())

        def modo_complejo():
            self.root.withdraw()
            subwindow = tk.Toplevel(self.root)
            ModoComplejo(subwindow).ejecutar()
            subwindow.protocol("WM_DELETE_WINDOW", lambda: self.root.deiconify())

        def modo_ecuacion_lineal():
            self.root.withdraw()
            subwindow = tk.Toplevel(self.root)
            ModoEcuacionLineal(subwindow).ejecutar()
            subwindow.protocol("WM_DELETE_WINDOW", lambda: self.root.deiconify())

        def modo_polinomios():
            self.root.withdraw()
            subwindow = tk.Toplevel(self.root)
            ModoPolinomios(subwindow).ejecutar()
            subwindow.protocol("WM_DELETE_WINDOW", lambda: self.root.deiconify())

        modo_normal_button = ttk.Button(self.root, text="Modo Normal", command=modo_normal)
        modo_normal_button.pack()

        modo_complejo_button = ttk.Button(self.root, text="Modo Complejo", command=modo_complejo)
        modo_complejo_button.pack()

        modo_ecuacion_lineal_button = ttk.Button(self.root, text="Modo Ecuación Lineal", command=modo_ecuacion_lineal)
        modo_ecuacion_lineal_button.pack()

        modo_polinomios_button = ttk.Button(self.root, text="Modo Polinomios", command=modo_polinomios)
        modo_polinomios_button.pack()

        salir_button = ttk.Button(self.root, text="Salir", command=self.root.quit)
        salir_button.pack()

        self.root.mainloop()

if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar_calculadora()
