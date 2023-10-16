

import random
import threading
class Modelo:
    
    gen=[]
    pesoIn = []
    #pesoIn_max = []
    #pesoIn_min = []
    nueva_gen_max = []
    nueva_gen_min = []
    
    mensajeMin = ""
    mensajeMax =""
    mensajeIni =""

    #random
    def generarRandom(self,PI, obj):
        nlista = []
        tamano=len(PI)
        for i in range(tamano):
            if i != obj:
                nlista.append(PI[i])
        return nlista

    #Metodo para calcular el peso
    #Metodo checado y correcto    
    def peso(self,w):
        
        x = w[0]
        y = w[1]
        z = w[2]
        
        p = pow(x,2) + pow(y,3) + pow(z,4)
        
        return p

    #Metodo llenado de poblacion inicial

    def poblacionInicial(self,inicial):
       
                
        valorIn = int(inicial)
        
        PI = [ [    [] for _ in range(3)]    for _ in range(valorIn)]
        
        val = 0
        
        for i in range(len(PI)):
            for j in range(3):
                val = random.randint(-10, 10)
                PI[i][j]= val
        
        self.mensajeIni += f"Esta es la ponblacion inicial: {PI}"
        
        for a in PI:
            
            p = self.peso(a)
            
            self.pesoIn.append(p)

        self.mensajeIni += f"\nEste es el peso inicial: {self.pesoIn}\n"
        
        return PI

    #Calculo de Wij = V1 + mu (v2 - v3)
    def calculoWij(self,list):
        w=[]
        op=[]
        
        for i in range(3):
            #print(ord_lista[i][0])
            for j in range(len(list)):
                op.append(list[j][i])

            w.append(op[0] + ((1/2)*(op[1] - op[2])))
            op=[]
        return w 
        
    def minimo (self,ord_lista,w,obj,PI):
        
        pesoGen = self.peso(w)
        pesoCom = self.pesoIn[obj]
        
        self.mensajeMin += ("\n\t\tDonde:")
        
        for i in range(len(ord_lista)) :
            
            self.mensajeMin += f"\n\t\t\tLa v {i+1}  es: {ord_lista[i]}"
        self.mensajeMin +=("") 
                
        var = ["x","y","z"]
        
        self.mensajeMin += ("\n\n\t\tEl vector W esta conformado por:")
        
        for i in range(len(w)):
            
            self.mensajeMin += f"\n\t\t\tLa w {var[i]} es: {w[i]}"
            
        #print("Este es w: ",w)
        self.mensajeMin +=("")
        self.mensajeMin += f"\n\n\t\tEste es el peso del objetivo: {pesoCom}\n"
        self.mensajeMin += f"\t\tEsto es el peso del vector W: {pesoGen}\n"

        self.mensajeMin +=("")
        if(pesoGen < pesoCom):
            self.pesoIn[obj] = pesoGen
            self.nueva_gen_max.append(w)
            self.mensajeMin += f"\n\t\tCambiamos el objetivo: {PI[obj]} \n\t\tpor el vector W: {w}\n"

        else:
            self.nueva_gen_max.append(PI[obj])
            self.mensajeMin +=("\n\t\tNo intercambiamo el objetivo por ningun vector W \n")
        
        
    #Metodo para calcular si es maximo

    def maximo (self,ord_lista,w,obj,PI):
        
        pesoGen = self.peso(w)
        pesoCom = self.pesoIn[obj]
        
        self.mensajeMax += ("\n\t\tDonde:")
        
        for i in range(len(ord_lista)) :
            
            self.mensajeMax += f"\n\t\t\tLa v {i+1}  es: {ord_lista[i]}"
        self.mensajeMax +=("") 
                
        var = ["x","y","z"]
        
        self.mensajeMax += ("\n\n\t\tEl vector W esta conformado por:")
        
        for i in range(len(w)):
            
            self.mensajeMax += f"\n\t\t\tLa w {var[i]} es: {w[i]}"
            
        #print("Este es w: ",w)
        self.mensajeMax +=("")
        self.mensajeMax += f"\n\n\t\tEste es el peso del objetivo: {pesoCom}\n"
        self.mensajeMax += f"\t\tEsto es el peso del vector W: {pesoGen}\n"

        self.mensajeMax +=("")
        if(pesoGen > pesoCom):
            self.pesoIn[obj] = pesoGen
            self.nueva_gen_max.append(w)
            self.mensajeMax += f"\n\t\tCambiamos el objetivo: {PI[obj]} \n\t\tpor el vector W: {w}\n"

        else:
            self.nueva_gen_max.append(PI[obj])
            self.mensajeMax +=("\n\t\tNo intercambiamo el objetivo por ningun vector W \n")
    
    
            
    #Metodo llenado de generacion
    def poblacionGeneracion(self,PI, obj):
        
        #elimina el obj de la lista para pdoer hacer la lista simulada de v1,v2,v3
        nlista = self.generarRandom(PI, obj)
        
        #Obtiene una nueva lista ordenada aletoriamnete y diferente a la original simulnado la eleccion de v1,v2,v3
        gen = random.sample(range(0,len(nlista)),3)
        
        ord_lista = []

        for i in range(len(gen)):
            x = gen[i]
            ord_lista.append(nlista[x])
        
        w = self.calculoWij(ord_lista)
        
        thread1 = threading.Thread(target=self.maximo(ord_lista,w,obj,PI))
        thread2 = threading.Thread(target=self.minimo(ord_lista,w,obj,PI))
        
        thread1.start()
        thread2.start()
        
        
    




    #Esto solo es para que funcione en consola
    """
    def main():
        global nueva_gen

        PI = poblacionInicial(4)

        for i in range(2):
            for j in range(len(PI)):
                poblacionGeneracion(PI, j)     
            print ("Esta es la ",i+1,"° generacion: ",nueva_gen,". Peso de esta generacion: ",pesoIn)
            nueva_gen = []

        
    if __name__ == "__main__":
        main()
    """
