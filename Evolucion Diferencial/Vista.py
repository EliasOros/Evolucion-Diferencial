import tkinter as tk
from tkinter import ttk

class Vista:
    
   def __init__(self):
        self.root = tk.Tk()
        self.root.title("Evolucion Diferencial")

   def crear_ventana_poblacion(self):
        self.label0 = tk.Label(self.root, text="Elige el tamaño de tu poblacion:")
        self.label0.grid(row=0, column=0, padx=10, pady=10)

        opciones_poblacion = ("4", "5", "6")
        self.spinbox_label0 = tk.Spinbox(self.root, values=opciones_poblacion)
        self.spinbox_label0.grid(row=0, column=1, padx=10, pady=10)

        self.button_label0 = tk.Button(self.root, text="Agregar", command=self.controlador_crear_poblacion)
        self.button_label0.grid(row=0, column=2)

   def crear_ventana_generaciones(self):
        self.label1 = tk.Label(self.root, text="Cuantas generaciones quieres hacer:")
        self.label1.grid(row=1, column=0, padx=10, pady=10)

        opciones_poblacion = ("2", "3")
        self.spinbox_label1 = tk.Spinbox(self.root, values=opciones_poblacion, state="disabled")
        self.spinbox_label1.grid(row=1, column=1, padx=10, pady=10)

        self.button_label1 = tk.Button(self.root, text="Calcular", command=self.controlador_crear_generaciones, state="disabled")
        self.button_label1.grid(row=1, column=2)
        
   def crear_boton_reinicio(self):
       self.button_reinicio = tk.Button(self.root,text =("Reiniciar"), command = self.reinciar, state="disabled")
       self.button_reinicio.grid(row = 2, column=1) 

   def iniciar(self):
        self.root.mainloop()
        
   def reinciar(self):
       self.button_reinicio.config(state="disabled")
       self.button_label0.config(state="active")
       self.button_label1.config(state="active")
       self.spinbox_label0.config(state="normal")

   def controlador_crear_poblacion(self):
        # Lógica para crear la población
        
        x = self.spinbox_label0.get()
        
        self.button_label0.config(state="disabled")
        self.button_label1.config(state="active")
        self.spinbox_label0.config(state="disabled")
        self.spinbox_label1.config(state="normal")
        
        return x

   def controlador_crear_generaciones(self):
        # Lógica para crear generaciones
        
        x = self.spinbox_label1.get()
        
        self.button_label1.config(state="disabled")
        self.button_reinicio.config(state="active")
        self.spinbox_label1.config(state="disabled")
        
        return x
