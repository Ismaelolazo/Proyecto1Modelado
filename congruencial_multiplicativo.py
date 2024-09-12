# congruencial_multiplicativo.py

import tkinter as tk
from math import log2

def congruencial_multiplicativo(semilla, a, g, cantidad_numeros, resultado_text):
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de texto
    semilla = int(semilla)
    a = int(a)
    g = int(g)
    cantidad_numeros = int(cantidad_numeros)
    
    # Calcular m = 2^g
    m = 2 ** g
    resultado_text.insert(tk.END, f"Semilla inicial X₀ = {semilla}\n")
    resultado_text.insert(tk.END, f"Parámetro a = {a}, m = {m}\n")
    
    if semilla % 2 == 0:
        resultado_text.insert(tk.END, "Error: La semilla debe ser un número impar.\n")
        return
    
    for i in range(cantidad_numeros):
        # Fórmula: X_{i+1} = (a * X_i) mod m
        semilla = (a * semilla) % m
        ri = semilla / (m - 1)
        resultado_text.insert(tk.END, f"Paso {i+1}: X{i+1} = ({a} * X{i}) mod {m} = {semilla}\n")
        resultado_text.insert(tk.END, f"Número pseudoaleatorio generado r{i+1} = {ri}\n")
        resultado_text.insert(tk.END, "-" * 50 + "\n")
