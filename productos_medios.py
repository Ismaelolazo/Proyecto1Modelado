# productos_medios.py
import tkinter as tk
def productos_medios(semilla_x0, semilla_x1, cantidad_numeros, resultado_text):
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de texto
    x0 = int(semilla_x0)
    x1 = int(semilla_x1)
    cantidad_numeros = int(cantidad_numeros)

    d = len(semilla_x0)  # Número de dígitos (D)
    
    resultado_text.insert(tk.END, f"Semilla X₀ = {x0}, Semilla X₁ = {x1}\n")
    
    for i in range(cantidad_numeros):
        # Multiplicar X₀ * X₁
        yi = x0 * x1
        resultado_text.insert(tk.END, f"Paso {i+1}: Y{i} = {x0} * {x1} = {yi}\n")
        
        # Convertir a cadena y extraer los D dígitos centrales
        yi_str = str(yi).zfill(2 * d)  # Asegurar que tenga 2D dígitos
        start = len(yi_str) // 2 - d // 2
        xi_plus_1 = int(yi_str[start:start + d])
        
        # Generar número pseudoaleatorio
        ri = xi_plus_1 / (10 ** d)
        resultado_text.insert(tk.END, f"Nueva semilla X{i+2} = {xi_plus_1}, Número pseudoaleatorio r{i} = {ri}\n")
        
        # Actualizar X₀ y X₁
        x0, x1 = x1, xi_plus_1
        resultado_text.insert(tk.END, "-" * 50 + "\n")
