import tkinter as tk

def productos_medios(semilla, cantidad_numeros, resultado_text):
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de texto
    semilla = int(semilla)
    cantidad_numeros = int(cantidad_numeros)
    
    resultado_text.insert(tk.END, f"Semilla inicial: {semilla}\n")
    
    for i in range(cantidad_numeros):
        cuadrado = semilla ** 2
        resultado_text.insert(tk.END, f"Paso {i+1}: Semilla {semilla} al cuadrado: {cuadrado}\n")
        
        cuadrado_str = str(cuadrado).zfill(8)  # Aseguramos que tenga 8 dígitos
        resultado_text.insert(tk.END, f"Número al cuadrado con ceros añadidos: {cuadrado_str}\n")
        
        # Seleccionamos los 4 dígitos centrales
        start = len(cuadrado_str) // 2 - 2
        semilla = int(cuadrado_str[start:start + 4])
        resultado_text.insert(tk.END, f"Nueva semilla (4 dígitos centrales): {semilla}\n")
        resultado_text.insert(tk.END, f"Número pseudoaleatorio generado: 0.{semilla}\n")
        resultado_text.insert(tk.END, "-" * 40 + "\n")
