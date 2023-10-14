

from Vista import Vista
from Modelo import Modelo
from VentanaEmergente import VentanaEmergente


class Controlador:
   
    PI = []
   
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista
        

    def iniciar(self):
        self.vista.crear_ventana_poblacion()
        self.vista.crear_ventana_generaciones()
        self.vista.crear_boton_reinicio()
        self.vista.iniciar()
        self.llamarCreacion()
        self.iniciarGeneraciones()
        
    def llamarCreacion(self):
        
        PI = self.modelo.poblacionInicial(4)
        NPI = ''.join(str(x) for x in PI)
        print(PI)
        print(NPI)
        
        return NPI
      
        
    def iniciarGeneraciones(self, PI):
        
        valorgen = self.vista.controlador_crear_generacion()
        generaciones_str = ""  # Crear una cadena vacía para almacenar las generaciones
        for i in range(valorgen):
            for j in range(len(PI)):
                self.modelo.poblacionGeneracion(PI, j)
            generaciones_str += f"Esta es la {i+1}° generación: {self.modelo.nueva_gen}. Peso de esta generación: {self.modelo.pesoIn}\n"
        
        return generaciones_str



if __name__ == "__main__":
    vista = Vista()
    modelo = Modelo()  # Crea una instancia del modelo
    
    controlador = Controlador(modelo, vista)  # Pasa el modelo, la ventana emergente y la vista al controlador
    controlador.iniciar()
    