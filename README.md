
# Evolucion Diferencial - Manual

Este programa esta diseñado para crear una poblacion de valores aleatorios asignando la cantidad de individuos y una numero de generaciones.

El programa esta diseñado para sacar los pesos de los valores elegidos mediante la siguiente funcion:

 	f(x) = x^2 + y^3 + z^4 

y la obtencion de los nuevos componentes del vector W mediante la formula

![imagen](https://github.com/EliasOros/Evolucion-Diferencial/assets/86860663/f27aa974-32ab-42d5-8274-a0ca8c826fa5)

	donde i = x,y,z

Obteniendo el peso de el vector W obtenido y comparandole con el vector objetivo, se decidira si se remplazara o no, ya sea si se desea maximizar o minimizar 

Este proceso se hace para todos los vectores ( de esta forma generando una nueva generacion), siempre colocando las v´s en algun vector aleatorio, (no importe si existen bastantes vectores y llegan a quedar unos sin v´s)

	0. El programa esta diseñado en base al paradigma orientado a objetos (POO) usando la arquitectura MVC (Modelo-Vista-Controlador) y el paradigma paralelo usando hilos 

Los pasos a seguir son:

	1. Elegir la cantidad de individuos que poblaran la poblacion inicial
 ![image](https://github.com/EliasOros/Evolucion-Diferencial/assets/111066628/e99b5fbc-45e6-493e-8ac9-d7a4c9a2d81b)

	2. Dar un click en el boton "Agregar", esto para generar la poblacion inicial
![image](https://github.com/EliasOros/Evolucion-Diferencial/assets/111066628/1877a8cd-5903-4b59-8006-fa3ff14c30a7)

	3. Seleccionar el numero de generaciones que se decee crear
![image](https://github.com/EliasOros/Evolucion-Diferencial/assets/111066628/a1131fb9-1d5d-4678-a6f7-cfb4cec83710)

	4. Dar un click en el boton "Calcular", esto para iniciar el proceso de las generaciones
 ![image](https://github.com/EliasOros/Evolucion-Diferencial/assets/111066628/7ae02881-68bf-4afc-8e1a-935eccb0d186)

Despues del paso 4, se abrira una nueva ventana con los resultados y procedimientos obtenidos, tanto del maximo y del minimo que se puede obtener a partir de la poblacion inicial

![imagen](https://github.com/EliasOros/Evolucion-Diferencial/assets/86860663/df5f6c4e-5c20-472d-8e80-3fcbee74ba54)

	5. Existe el boton de reinicio, que permitira al usuario regresar al paso 1, y al llegar al finalizar el paso 4, se mostrara una ventana con estos nuevos valores, sin eliminar la ventana anterior


