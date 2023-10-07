import tkinter as tk
from tkinter import ttk

##adiossss

root = tk.Tk()
root.title("Evolucion Diferencial")

label0 = tk.Label(root, text = ("Elige el tamaño de tu poblacion:"))
label0.grid(row=0,column=0,padx=10, pady=10)

opcionesPoblacion = ("4","5","6")

spinbox_label0 = tk.Spinbox(root, values = opcionesPoblacion)
spinbox_label0.grid(row=0,column=1, padx=10, pady=10)

def crearPoblacion():
    
    print("hola")
    
    button_label0.config(state="disabled")
    button_label1.config(state="active")
    spinbox_label0.config(state="disabled")
    spinbox_label1.config(state="normal")


button_label0 = tk.Button(root, text =("Agregar"), command = crearPoblacion  )
button_label0.grid(row=0,column=2)


label1 = tk.Label(root, text = ("Cuantas generaciones quieres hacer:"))
label1.grid(row=1,column=0,padx=10, pady=10)

opcionesPoblacion = ("2","3")

spinbox_label1 = tk.Spinbox(root, values = opcionesPoblacion, state="disabled")
spinbox_label1.grid(row=1,column=1, padx=10, pady=10)

def crearGeneracionesPoblacion():
    
    print("hola")
    
    button_label1.config(state="disabled")
    button_reinicio.config(state="active")
    spinbox_label1.config(state="disabled")


button_label1 = tk.Button(root, text =("Calcular"), command = crearGeneracionesPoblacion, state="disabled"  )
button_label1.grid(row=1,column=2)


def reinciar():
    
    print("hola")
    button_reinicio.config(state="disabled")
    button_label0.config(state="active")
    button_label1.config(state="active")
    spinbox_label0.config(state="normal")
    

button_reinicio = tk.Button(root,text =("Reiniciar"), command = reinciar, state="disabled")
button_reinicio.grid(row = 2, column=1)


root.mainloop()

