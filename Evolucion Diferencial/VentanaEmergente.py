import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

root.title("Resultados")

root.geometry("900x600")

frame0 = tk.Frame(root, borderwidth=2,relief="ridge")
frame0.pack(padx=10, pady=10, side="left")

frame1 = tk.Frame(root, borderwidth=2,relief="ridge")
frame1.pack(padx=10, pady=10, side="right")


label0 = tk.Label(frame0, text=("Minimo"))
label0.pack(padx=10, pady=10)

label1 = tk.Label(frame1, text=("Maximo"))
label1.pack(padx=10, pady=10)

# Crear un widget ScrolledText dentro del frame
scroll_minimo = scrolledtext.ScrolledText(frame0, wrap=tk.WORD, width=50, height=50, state="disabled")
scroll_minimo.pack(padx=10,pady=10)

# Crear un widget ScrolledText dentro del frame
scroll_maximo = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=50, height=50, state="disabled")
scroll_maximo.pack(padx=10,pady=10)


def imprimir_en_scrollMin(mensaje):
    scroll_minimo.config(state=tk.NORMAL)  # Habilitar la edición del widget
    scroll_minimo.insert(tk.END, mensaje)  # Insertar el mensaje al final del widget
    scroll_minimo.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
    scroll_minimo.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir
    
    
def imprimir_en_scrollMax(mensaje):
    scroll_maximo.config(state=tk.NORMAL)  # Habilitar la edición del widget
    scroll_maximo.insert(tk.END, mensaje)  # Insertar el mensaje al final del widget
    scroll_maximo.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
    scroll_maximo.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir
    
    

root.mainloop()
