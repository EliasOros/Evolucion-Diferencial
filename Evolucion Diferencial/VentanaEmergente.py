import tkinter as tk
from tkinter import scrolledtext

class VentanaEmergente:
    
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Resultados")
        self.root.geometry("900x600")

    def generarventana(self):
        
        

        frame = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame.pack(padx=10, pady=10, side="top")

        frame0 = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame0.pack(padx=10, pady=10, side="left")

        frame1 = tk.Frame(self.root, borderwidth=2, relief="ridge")
        frame1.pack(padx=10, pady=10, side="right")

        self.label = tk.Label(frame, text="Poblacion incial:")
        self.label.pack(padx=10, pady=10, side="top")

        self.label0 = tk.Label(frame0, text="Minimo")
        self.label0.grid(row=0, column=1, padx=10, pady=10)

        self.label1 = tk.Label(frame1, text="Maximo")
        self.label1.grid(row=0, column=1, padx=10, pady=10)

        # Crear un widget ScrolledText dentro del frame
        self.scroll_minimo = scrolledtext.ScrolledText(frame0, wrap=tk.WORD, width=50, height=20, state="disabled")
        self.scroll_minimo.grid(row=1, column=1, padx=10, pady=10)

        # Crear un widget ScrolledText dentro del frame
        self.scroll_maximo = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=50, height=20, state="disabled")
        self.scroll_maximo.grid(row=1, column=1, pady=10)

        self.labelMinimo = tk.Label(frame0, text="Poblacion final minimo:")
        self.labelMinimo.grid(row=2, column=1, padx=10, pady=10)

        self.labelMaximo = tk.Label(frame1, text="Poblacion final maximizar:")
        self.labelMaximo.grid(row=2, column=1, padx=10, pady=10)

    def iniciar(self):
        self.root.mainloop()

    def imprimirPoblacionInicial(self, poblacion_inicial):
        
        self.label.config(text=poblacion_inicial)
        
        
    def imprimirPoblacionMinima(poblacionInicial):
        
        print("")
        
    def imprimirPoblacionMaxima(poblacionInicial):
        
        print("")


    def imprimir_en_scroll_min(self, mensaje):
        self.scroll_minimo.config(state=tk.NORMAL)  # Habilitar la edición del widget
        self.scroll_minimo.insert(tk.END, mensaje)  # Insertar el mensaje al final del widget
        self.scroll_minimo.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
        self.scroll_minimo.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir

    def imprimir_en_scroll_max(self, mensaje):
        self.scroll_maximo.config(state=tk.NORMAL)  # Habilitar la edición del widget
        self.scroll_maximo.insert(tk.END, mensaje)  # Insertar el mensaje al final del widget
        self.scroll_maximo.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
        self.scroll_maximo.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir

'''        
if __name__ == "__main__":
    ventana_emergente = VentanaEmergente()  # Crea una instancia de la clase
    ventana_emergente.generarventana()  # Crea y configura la ventana primero

    # Luego, puedes llamar a otros métodos para mostrar contenido en la ventana
    poblacion_inicial = "Población inicial: [1, 2, 3, 4, 5]"
    mensaje_minimo = "Resultado mínimo: 42"
    mensaje_maximo = "Resultado máximo: 100"

    ventana_emergente.imprimirPoblacionInicial(poblacion_inicial)
    ventana_emergente.imprimir_en_scroll_min(mensaje_minimo)
    ventana_emergente.imprimir_en_scroll_max(mensaje_maximo)
    
    ventana_emergente.iniciar()  # Finalmente, inicia el bucle principal de la ventana'''

  
