#controlador
from Modelo import poblacionInicial, poblacionGeneracion
##from VentanaEmergente import imprimir
import Modelo


PI = []
def llamarCreacion(inicial):
    global PI
    PI = poblacionInicial(inicial)
    





def iniciarGeneraciones(gen):
    valorgen = int(gen)
    for i in range(valorgen):
        for j in range (len(PI)):
            poblacionGeneracion(PI,j)
        print ("Esta es la ",i+1,"° generacion: ",Modelo.nueva_gen,". Peso de esta generacion: ",Modelo.pesoIn)
        

