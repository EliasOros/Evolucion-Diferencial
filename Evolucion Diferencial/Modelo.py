

import random
class Modelo:
    
    gen=[]
    pesoIn = []
    nueva_gen = []

    #random
    def generarRandom(self,PI, obj):
        nlista = []
        tamano=len(PI)
        for i in range(tamano):
            if i != obj:
                nlista.append(PI[i])
        return nlista

    #Metodo para calcular el peso
   
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
        
        print ("Este es la ponblacion inicial: ",PI)
        
        for a in PI:
            
            p = self.peso(a)
            
            self.pesoIn.append(p)

        print ("Este es el peso inicial: ",self.pesoIn,"\n")
        
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

    
        
    #Metodo para calcular si es minimo
    def minimo(self,w,obj,PI):
        
        pesoGen = self.peso(w)
        pesoCom = self.pesoIn[obj]
        print("Este es w: ",w)
        print("Esto es el peso inicial: ",pesoCom)
        print("Esto es el peso a comparar: ",pesoGen)
        print("El objetivo: ", obj,"\n")
        if(pesoGen < pesoCom):
            self.pesoIn[obj] = pesoGen
            self.nueva_gen.append(w)
            print("Cambiamos por w \n")
        else:
            self.nueva_gen.append(PI[obj])
            print("Dejamos el anterior \n")
        
        
    #Metodo para calcular si es maximo

    def maximo (self,w,obj,PI):
        pesoGen = self.peso(w)
        pesoCom = self.pesoIn[obj]
        print("Este es w: ",w)
        print("Esto es el peso inicial: ",pesoCom)
        print("Esto es el peso a comparar: ",pesoGen)
        print("El objetivo: ", obj,"\n")
        if(pesoGen > pesoCom):
            self.pesoIn[obj] = pesoGen
            self.nueva_gen.append(w)
            print("Cambiamos por w \n")
        else:
            self.nueva_gen.append(PI[obj])
            print("Dejamos el anterior \n")
            
    #Metodo llenado de generacion
    def poblacionGeneracion(self,PI, obj):
        
        nlista = self.generarRandom(PI, obj)
        gen = random.sample(range(0,len(nlista)),3)
        
        ord_lista = []

        for i in range(len(gen)):
            x = gen[i]
            ord_lista.append(nlista[x])
        
        w = self.calculoWij(ord_lista)
        
        self.maximo(w,obj,PI)
        

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
