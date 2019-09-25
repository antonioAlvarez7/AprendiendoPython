#Importamos la libreria "random"
import random
#Creamos una variable de tipo float llamada numero1
numero1 = float (10.5)
#Creamos una funcion
def mifuncion():
    numero2 = float (random.randrange(1,10))
    mensaje="la suma de  {} y {} es {}"
    print (mensaje.format(numero1,numero2,numero1+numero2))
#Se ejecuta la funcion que creamos
    mifuncion()