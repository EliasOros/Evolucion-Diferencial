

from Vista import Vista
from Modelo import Modelo
from VentanaEmergente import VentanaEmergente



class Controlador:
   
    PI = []
   
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista
        self.PI = None
        
        

    def iniciar(self):
     
        self.vista.iniciar()
        self.llamarCreacion()
        self.iniciarGeneraciones()
        
    def llamarCreacion(self):
        
        if self.PI is None:
                  
            self.PI = self.modelo.poblacionInicial(self.vista.controlador_crear_poblacion())

        NPI = ''.join(str(x) for x in self.PI)

        return self.PI
    
        #print(PI)
        #print(NPI)
        
        

      
        
    def iniciarGeneraciones(self):
        valorgen = int(self.vista.controlador_crear_generaciones())
        generaciones_str = ""  # Crear una cadena vacía para almacenar las generaciones
        PI = self.llamarCreacion()  # Obtén la población inicial
        for i in range(valorgen):
            for j in range(len(PI)):
                self.modelo.poblacionGeneracion(PI, j)
            generaciones_str += f"Esta es la {i+1}° generación: {self.modelo.nueva_gen}. Peso de esta generación: {self.modelo.pesoIn}\n"
        return generaciones_str




if __name__ == "__main__":
    modelo = Modelo()
    controlador = Controlador(modelo, None)  # Puedes dejar None como argumento temporalmente
    vista = Vista(controlador)  # Ahora pasamos el controlador al crear la vista
    controlador.vista = vista  # Asignamos la vista al controlador
    controlador.iniciar()