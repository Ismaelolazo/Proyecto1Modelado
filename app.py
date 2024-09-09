import tkinter as tk
from productos_medios import productos_medios
from congruencial_lineal import congruencial_lineal
from cuadrados_medios import cuadrados_medios

# Funciones para mostrar solo los campos necesarios
def mostrar_campos_cuadrados_medios():
    ocultar_todos_los_campos()
    label_semilla.grid(row=1, column=0)
    entry_semilla.grid(row=1, column=1)
    label_cantidad.grid(row=2, column=0)
    entry_cantidad.grid(row=2, column=1)
    button_ejecutar_cuadrados_medios.grid(row=3, column=0, columnspan=2)

def mostrar_campos_productos_medios():
    ocultar_todos_los_campos()
    label_semilla_x0.grid(row=1, column=0)
    entry_semilla_x0.grid(row=1, column=1)
    label_semilla_x1.grid(row=2, column=0)
    entry_semilla_x1.grid(row=2, column=1)
    label_cantidad.grid(row=3, column=0)
    entry_cantidad.grid(row=3, column=1)
    button_ejecutar_productos_medios.grid(row=4, column=0, columnspan=2)

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
    label_semilla_x0.grid_forget()
    entry_semilla_x0.grid_forget()
    label_semilla_x1.grid_forget()
    entry_semilla_x1.grid_forget()
    button_ejecutar_productos_medios.grid_forget()
    button_ejecutar_congruencial_lineal.grid_forget()
    button_ejecutar_cuadrados_medios.grid_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Números Pseudoaleatorios")

# Menú con opciones desplegables
frame_menu = tk.Frame(root)
frame_menu.grid(row=0, column=0, columnspan=2, pady=10)

# Menú desplegable para métodos no congruenciales
menu_no_congruenciales = tk.Menubutton(frame_menu, text="NO Congruenciales", relief="raised")
menu_no_congruenciales.menu = tk.Menu(menu_no_congruenciales, tearoff=0)
menu_no_congruenciales["menu"] = menu_no_congruenciales.menu

menu_no_congruenciales.menu.add_command(label="Cuadrados Medios", command=mostrar_campos_cuadrados_medios)
menu_no_congruenciales.menu.add_command(label="Productos Medios", command=mostrar_campos_productos_medios)
menu_no_congruenciales.grid(row=0, column=0)

# Menú desplegable para métodos congruenciales
menu_congruenciales = tk.Menubutton(frame_menu, text="Congruenciales", relief="raised")
menu_congruenciales.menu = tk.Menu(menu_congruenciales, tearoff=0)
menu_congruenciales["menu"] = menu_congruenciales.menu

menu_congruenciales.menu.add_command(label="Lineal", command=mostrar_campos_congruencial_lineal)
menu_congruenciales.menu.add_command(label="Multiplicativo", command=lambda: resultado_text.insert(tk.END, "Método Congruencial Multiplicativo aún no implementado.\n"))
menu_congruenciales.grid(row=0, column=1)

# Etiquetas y campos de entrada
label_semilla = tk.Label(root, text="Semilla:")
entry_semilla = tk.Entry(root)

label_cantidad = tk.Label(root, text="Cantidad de Números:")
entry_cantidad = tk.Entry(root)

label_a = tk.Label(root, text="a (Multiplicador):")
entry_a = tk.Entry(root)

label_c = tk.Label(root, text="c (Incremento):")
entry_c = tk.Entry(root)

# Etiquetas para Productos Medios
label_semilla_x0 = tk.Label(root, text="Semilla X₀:")
entry_semilla_x0 = tk.Entry(root)

label_semilla_x1 = tk.Label(root, text="Semilla X₁:")
entry_semilla_x1 = tk.Entry(root)

# Botones de ejecutar
button_ejecutar_cuadrados_medios = tk.Button(root, text="Ejecutar", 
                                             command=lambda: cuadrados_medios(entry_semilla.get(), entry_cantidad.get(), resultado_text))

button_ejecutar_productos_medios = tk.Button(root, text="Ejecutar", 
                                             command=lambda: productos_medios(entry_semilla_x0.get(), entry_semilla_x1.get(), entry_cantidad.get(), resultado_text))

button_ejecutar_congruencial_lineal = tk.Button(root, text="Ejecutar", 
                                                command=lambda: congruencial_lineal(entry_semilla.get(), entry_cantidad.get(), entry_a.get(), entry_c.get(), resultado_text))

# Área de texto para mostrar el resultado
resultado_text = tk.Text(root, height=15, width=70)
resultado_text.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar el bucle de la aplicación
root.mainloop()
