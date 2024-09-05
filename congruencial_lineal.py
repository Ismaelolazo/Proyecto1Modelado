# congruencial_lineal.py

import tkinter as tk
from math import gcd, log  # Para calcular el MCD y logaritmo natural

# Verificación de los parámetros del método congruencial lineal
def verificar_parametros(a, c, m, resultado_text):
    if (m & (m - 1)) != 0:
        resultado_text.insert(tk.END, f"Error: m = {m} no es una potencia de 2.\n")
        return False
    if (a - 1) % 4 != 0:
        resultado_text.insert(tk.END, f"Error: a = {a} no cumple la condición a = 1 + 4k.\n")
        return False
    if gcd(c, m) != 1:
        resultado_text.insert(tk.END, f"Error: c = {c} no es relativamente primo con m = {m}.\n")
        return False
    resultado_text.insert(tk.END, "Los parámetros son válidos.\n")
    return True

# Función para calcular el valor de m automáticamente
def calcular_m(cantidad_numeros):
    g = log(cantidad_numeros) / log(2)
    m = 2 ** int(g)
    return m

# Método congruencial lineal
def congruencial_lineal(semilla, cantidad_numeros, a, c, resultado_text):
    resultado_text.delete(1.0, tk.END)
    semilla = int(semilla)
    a = int(a)
    c = int(c)
    cantidad_numeros = int(cantidad_numeros)
    
    # Calcular m basado en la cantidad de números
    m = calcular_m(cantidad_numeros)
    
    resultado_text.insert(tk.END, f"Valor calculado de m = {m}\n")
    
    if not verificar_parametros(a, c, m, resultado_text):
        return
    
    resultado_text.insert(tk.END, f"Semilla inicial: {semilla}\n")
    resultado_text.insert(tk.END, f"Parámetros: a={a}, c={c}, m={m}\n")
    
    for i in range(1, cantidad_numeros + 1):
        semilla = (a * semilla + c) % m
        numero_pseudoaleatorio = semilla / m
        resultado_text.insert(tk.END, f"Paso {i}: X{i} = ({a} * X{i-1} + {c}) mod {m} = {semilla}\n")
        resultado_text.insert(tk.END, f"    Número pseudoaleatorio generado: {numero_pseudoaleatorio:.4f}\n")
        resultado_text.insert(tk.END, "-" * 50 + "\n")
