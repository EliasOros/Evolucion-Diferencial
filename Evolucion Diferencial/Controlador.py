

import threading
from Vista import Vista
from Modelo import Modelo
from VentanaEmergente import VentanaEmergente



class Controlador:
   
    PI = []
    mensajeFinmax = ""  # Crear una cadena vacía para almacenar las generaciones
    mensajeFinmin = ""  # Crear una cadena vacía para almacenar las generaciones
   
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
     
     
    
    def iniciarGeneraciones(self):
        
        valorgen = int(self.vista.controlador_crear_generaciones())
        
        PI = self.llamarCreacion()  # Obtén la población inicial
        
        PI_max = PI
        PI_min = PI
        
        for i in range(valorgen):
            
            
            
            self.modelo.mensajeMax += f"\nPara la generacion {i+1}\n"
            self.modelo.mensajeMin += f"\nPara la generacion {i+1}\n"
            
            self.modelo.nueva_gen_min = []
            self.modelo.nueva_gen_max = []
         
            thread1 = threading.Thread(target=self.generacionMax, args=(PI_max,))
            thread2 = threading.Thread(target=self.generacionMin, args=(PI_min,))
            thread1.start()
            thread2.start()
            thread1.join()  # Espera a que thread1 termine
            thread2.join()  # Espera a que thread2 termine

            print ("PI:",PI)
            print ("PI-MAX",PI_max)
            
            # Actualizar PI con las nuevas generaciones correspondientes
            PI_max = self.modelo.nueva_gen_max
            PI_min = self.modelo.nueva_gen_min
            
            print ("Pi-Max2",PI_max)
    
            #print ("La generacion", i+1,"queda de la siguiente forma", self.modelo.nueva_gen,"con peso", self.modelo.pesoIn ,"\n")
            self.mensajeFinmax += f"La {i+1}° generación es: {self.modelo.nueva_gen_max}.  \n\t El peso de la generación es: {self.modelo.obtencionpeso(PI_max)}\n\n"
            self.mensajeFinmin += f"La {i+1}° generación es: {self.modelo.nueva_gen_min}.  \n\t El peso de la generación es: {self.modelo.obtencionpeso(PI_min)}\n\n"
            
            print (self.mensajeFinmax)
            print(self.mensajeFinmin)
            
            
         
        ventanaEmergente = VentanaEmergente()
        ventanaEmergente.generarVentana()  
        ventanaEmergente.imprimirPoblacionInicial(self.modelo.mensajeIni)
        ventanaEmergente.imprimir_en_scroll_max(self.modelo.mensajeMax) 
        ventanaEmergente.imprimir_en_scroll_min(self.modelo.mensajeMin) 
        ventanaEmergente.imprimirPoblacionMaxima(self.mensajeFinmax)
        ventanaEmergente.imprimirPoblacionMinima(self.mensajeFinmin)
        
    def generacionMax(self, PI_max):
        
                 
        for j in range(len(PI_max)):
              
                
            self.modelo.mensajeMax += f"\n\tPara el objetivo: {PI_max[j]} \n"
                
            self.modelo.poblacionGeneracionMax(PI_max, j)   
        
    def generacionMin(self, PI_min):
        
      
        for j in range(len(PI_min)):
                
                
            self.modelo.mensajeMin += f"\n\tPara el objetivo: {PI_min[j]} \n"
            self.modelo.poblacionGeneracionMin(PI_min, j)
            
    def reiniciar(self):
        
        self.vista.reiniciar()
        self.PI = None
        self.mensajeFinmax = ""
        self.mensajeFinmin = ""
        self.modelo.mensajeMin = ""
        self.modelo.mensajeMax = ""
        self.modelo.mensajeIni = ""
        self.modelo.pesoIn = []
        self.modelo.nueva_gen_max = []
        self.modelo.nueva_gen_min = []
        self.modelo.gen = []
        
        
                  
if __name__ == "__main__":
    modelo = Modelo()
    controlador = Controlador(modelo, None)  # Puedes dejar None como argumento temporalmente
    vista = Vista(controlador)  # Ahora pasamos el controlador al crear la vista
    controlador.vista = vista  # Asignamos la vista al controlador
    controlador.iniciar()