

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
        mensajeFinmax = ""  # Crear una cadena vacía para almacenar las generaciones
        PI = self.llamarCreacion()  # Obtén la población inicial
        
        for i in range(valorgen):
            
            
            self.modelo.mensajeMax += f"Para la generacion {i+1}\n"

            self.modelo.nueva_gen = []
            
            for j in range(len(PI)):
                
                self.modelo.mensajeMax += f"Para el objetivo: {PI[j]} \n"
                self.modelo.poblacionGeneracion(PI, j)
        
            PI = self.modelo.nueva_gen
            print ("La generacion", i+1,"queda de la siguiente forma", self.modelo.nueva_gen,"con peso", self.modelo.pesoIn ,"\n")
            mensajeFinmax += f"La {i+1}° generación es: {self.modelo.nueva_gen}.  \n y el peso de esta generación: {self.modelo.pesoIn}\n"
        
            
         
        ventanaEmergente = VentanaEmergente()
        ventanaEmergente.generarVentana()  
        ventanaEmergente.imprimirPoblacionInicial(self.modelo.mensajeIni)
        ventanaEmergente.imprimir_en_scroll_max(self.modelo.mensajeMax) 
        ventanaEmergente.imprimirPoblacionMaxima(mensajeFinmax)
        
        
        
    
  
if __name__ == "__main__":
    modelo = Modelo()
    controlador = Controlador(modelo, None)  # Puedes dejar None como argumento temporalmente
    vista = Vista(controlador)  # Ahora pasamos el controlador al crear la vista
    controlador.vista = vista  # Asignamos la vista al controlador
    controlador.iniciar()