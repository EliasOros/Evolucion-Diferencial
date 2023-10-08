
###############################################################################################
###############################           ATRIBUTOS          ##################################
import random

gen=[]
pesoIn = []
nueva_gen = []

#Metodo para calcular el peso

def peso(w):
    x = w[0]
    y = w[1]
    z = w[2]
    
    p = pow(x,2) + pow(y,3) + pow(z,4)
    return p
    
#Metodo para calcular si es minimo

def minimo():
    
    print ("minimo")
    
#Metodo para calcular si es maximo

def maximo (w,obj,PI):
    pesoGen = peso(w)
    pesoCom = pesoIn[obj]
    print("Este es w: ",w)
    print("Esto es el peso inicial: ",pesoCom)
    print("Esto es el peso a comparar: ",pesoGen)
    print("El objetivo: ", obj,"\n")
    if(pesoGen > pesoCom):
        pesoIn[obj] = pesoGen
        nueva_gen.append(w)
        print("Cambiamos por w \n")
    else:
        nueva_gen.append(PI[obj])
        print("Dejamos el anterior \n")
    
#Metodo llenado de poblacion inicial

def poblacionInicial(inicial):
    global pesoIn
    valorIn = int(inicial)
    PI = [[[] for _ in range(3)] for _ in range(valorIn)]
    val = 0
    for i in range(len(PI)):
        for j in range(3):
            val = random.randint(-10, 10)
            PI[i][j]= val
    
    print ("Este es la ponblacion inicial: ",PI)
    for a in PI:
        p = peso(a)
        pesoIn.append(p)

    print ("Este es el peso inicial: ",pesoIn,"\n")
    return PI
    
#Metodo llenado de generacion

def poblacionGeneracion(PI, obj):
    
    nlista = generarRandom(PI, obj)
    gen = random.sample(range(0,len(nlista)),3)
    
    ord_lista = []

    for i in range(len(gen)):
        x = gen[i]
        ord_lista.append(nlista[x])
    
    w = operacio(ord_lista)
    
    maximo(w,obj,PI)
    
#Metodo eleccion de objetivo y vs

def eleccionObjVs():
    
    print("Wuenas")



def generarRandom(PI, obj):
    nlista = []
    tamano=len(PI)
    for i in range(tamano):
        if i != obj:
            nlista.append(PI[i])
    return nlista



def operacio(list):
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