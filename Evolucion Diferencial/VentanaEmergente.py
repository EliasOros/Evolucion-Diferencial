from msilib.schema import Font
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

class VentanaEmergente:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resultados")
        self.root.geometry("1350x650")
        self.root.config(bg="#ececec")

    def generarVentana(self):
        
        fuente_negrita = ("Helvetica", 9, "bold")
        
        frame = tk.Frame(self.root, borderwidth=2, relief="ridge",bg="#c2dfdd")
        frame.pack(padx=10, pady=10, side="top")

        frame0 = tk.Frame(self.root, borderwidth=2, relief="ridge",bg="#c2dfdd")
        frame0.pack(padx=10, pady=10, side="left")

        frame1 = tk.Frame(self.root, borderwidth=2, relief="ridge",bg="#c2dfdd")
        frame1.pack(padx=10, pady=10, side="right")

        self.label = tk.Label(frame,bg="#c2dfdd",font=fuente_negrita)
        self.label.pack(padx=10, pady=10, side="top")

        self.label0 = tk.Label(frame0, text="Minimo",bg="#c2dfdd",font=fuente_negrita)
        self.label0.grid(row=0, column=1, padx=10, pady=10)

        self.label1 = tk.Label(frame1, text="Maximo",bg="#c2dfdd",font=fuente_negrita)
        self.label1.grid(row=0, column=1, padx=10, pady=10)

        # Crear un widget ScrolledText dentro del frame
        self.scroll_minimo = scrolledtext.ScrolledText(frame0, wrap=tk.WORD, width=70, height=20, state="disabled",bg="#15e295")
        self.scroll_minimo.grid(row=1, column=1, padx=10, pady=10)

        # Crear un widget ScrolledText dentro del frame
        self.scroll_maximo = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=70, height=20, state="disabled",bg="#15e295")
        self.scroll_maximo.grid(row=1, column=1, pady=10)
        
        # Crear un widget ScrolledText dentro del frame
        self.scroll_maximo_res = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=80, height=8, state="disabled",bg="#c2dfdd",font=fuente_negrita)
        self.scroll_maximo_res.grid(row=2, column=1, pady=10)
        
        # Crear un widget ScrolledText dentro del frame
        self.scroll_minimo_res = scrolledtext.ScrolledText(frame0, wrap=tk.WORD, width=80, height=8, state="disabled",bg="#c2dfdd",font=fuente_negrita)
        self.scroll_minimo_res.grid(row=2, column=1, pady=10)

        '''self.labelMinimo = tk.Label(frame0, text="Poblacion final minimo:",bg="#c2dfdd",font=fuente_negrita)
        self.labelMinimo.grid(row=2, column=1, padx=10, pady=10)

        self.labelMaximo = tk.Label(frame1, text="Poblacion final maximizar:",bg="#c2dfdd",font=fuente_negrita)
        self.labelMaximo.grid(row=2, column=1, padx=10, pady=10)
'''
    def iniciar(self):
        ventana_emergente = VentanaEmergente()  # Crea una instancia de la clase
        ventana_emergente.generarVentana()  # Crea y configura la ventana primero

        # Luego, puedes llamar a otros métodos para mostrar contenido en la ventana
        poblacion_inicial = "Población inicial: [1, 2, 3, 4, 5]"
        mensaje_minimo = "Resultado mínimo: 42"
        mensaje_maximo = "Resultado máximo: 100"

        ventana_emergente.imprimirPoblacionInicial(poblacion_inicial)
        ventana_emergente.imprimir_en_scroll_min(mensaje_minimo)
        ventana_emergente.imprimir_en_scroll_max(mensaje_maximo)
        self.root.mainloop()

    def imprimirPoblacionInicial(self,mensajeIni):
        
        self.label.config(text=(mensajeIni))
        
        
    def imprimirPoblacionMinima(self,mensajeFinMin):
        
        self.scroll_minimo_res.config(state=tk.NORMAL)  # Habilitar la edición del widget
        self.scroll_minimo_res.insert(tk.END, mensajeFinMin)  # Insertar el mensaje al final del widget
        self.scroll_minimo_res.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
        self.scroll_minimo_res.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir
        
        #self.labelMinimo.config(text=mensajeFinMin)
        
    def imprimirPoblacionMaxima(self,mensajeFinMax):
        
        self.scroll_maximo_res.config(state=tk.NORMAL)  # Habilitar la edición del widget
        self.scroll_maximo_res.insert(tk.END, mensajeFinMax)  # Insertar el mensaje al final del widget
        self.scroll_maximo_res.see(tk.END)  # Hacer que el widget muestre automáticamente el contenido nuevo
        self.scroll_maximo_res.config(state=tk.DISABLED)  # Deshabilitar la edición del widget después de imprimir
        
        #self.labelMaximo.config(text=mensajeFinMax)

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

'''if __name__ == "__main__":
    ventana_emergente = VentanaEmergente() 
    ventana_emergente.iniciar()
     '''
'''if __name__ == "__main__":
    ventana_emergente = VentanaEmergente()  # Crea una instancia de la clase
    ventana_emergente.generarVentana()  # Crea y configura la ventana primero

    # Luego, puedes llamar a otros métodos para mostrar contenido en la ventana
    poblacion_inicial = "Población inicial: [1, 2, 3, 4, 5]"
    mensaje_minimo = "Resultado mínimo: 42"
    mensaje_maximo = "Resultado máximo: 100"

    ventana_emergente.imprimirPoblacionInicial(poblacion_inicial)
    ventana_emergente.imprimir_en_scroll_min(mensaje_minimo)
    ventana_emergente.imprimir_en_scroll_max(mensaje_maximo)
    
    ventana_emergente.iniciar()  # Finalmente, inicia el bucle principal de la ventana'''

  
