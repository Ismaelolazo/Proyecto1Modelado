# main.py

import tkinter as tk
from productos_medios import productos_medios
from congruencial_lineal import congruencial_lineal

# Funciones para mostrar solo los campos necesarios
def mostrar_campos_productos_medios():
    ocultar_todos_los_campos()
    label_semilla.grid(row=1, column=0)
    entry_semilla.grid(row=1, column=1)
    label_cantidad.grid(row=2, column=0)
    entry_cantidad.grid(row=2, column=1)
    button_ejecutar_productos_medios.grid(row=3, column=0, columnspan=2)

def mostrar_campos_congruencial_lineal():
    ocultar_todos_los_campos()
    label_semilla.grid(row=1, column=0)
    entry_semilla.grid(row=1, column=1)
    label_a.grid(row=2, column=0)
    entry_a.grid(row=2, column=1)
    label_c.grid(row=3, column=0)
    entry_c.grid(row=3, column=1)
    label_cantidad.grid(row=4, column=0)
    entry_cantidad.grid(row=4, column=1)
    button_ejecutar_congruencial_lineal.grid(row=5, column=0, columnspan=2)

def ocultar_todos_los_campos():
    label_semilla.grid_forget()
    entry_semilla.grid_forget()
    label_cantidad.grid_forget()
    entry_cantidad.grid_forget()
    label_a.grid_forget()
    entry_a.grid_forget()
    label_c.grid_forget()
    entry_c.grid_forget()
    button_ejecutar_productos_medios.grid_forget()
    button_ejecutar_congruencial_lineal.grid_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Números Pseudoaleatorios")

# Menú con 2 botones para los métodos
frame_menu = tk.Frame(root)
frame_menu.grid(row=0, column=0, columnspan=2, pady=10)

button_productos_medios = tk.Button(frame_menu, text="Método de Productos Medios", command=mostrar_campos_productos_medios)
button_productos_medios.grid(row=0, column=0)

button_congruencial_lineal = tk.Button(frame_menu, text="Método Congruencial Lineal", command=mostrar_campos_congruencial_lineal)
button_congruencial_lineal.grid(row=0, column=1)

# Etiquetas y campos de entrada
label_semilla = tk.Label(root, text="Semilla:")
entry_semilla = tk.Entry(root)

label_cantidad = tk.Label(root, text="Cantidad de Números:")
entry_cantidad = tk.Entry(root)

label_a = tk.Label(root, text="a (Multiplicador):")
entry_a = tk.Entry(root)

label_c = tk.Label(root, text="c (Incremento):")
entry_c = tk.Entry(root)

# Botones de ejecutar
button_ejecutar_productos_medios = tk.Button(root, text="Ejecutar", 
                                             command=lambda: productos_medios(entry_semilla.get(), entry_cantidad.get(), resultado_text))
button_ejecutar_congruencial_lineal = tk.Button(root, text="Ejecutar", 
                                                command=lambda: congruencial_lineal(entry_semilla.get(), entry_cantidad.get(), entry_a.get(), entry_c.get(), resultado_text))

# Área de texto para mostrar el resultado
resultado_text = tk.Text(root, height=15, width=70)
resultado_text.grid(row=6, column=0, columnspan=2, pady=10)

# Mostrar solo los campos de datos necesarios al inicio
mostrar_campos_productos_medios()

# Iniciar el bucle de la aplicación
root.mainloop()
