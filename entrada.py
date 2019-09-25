entrada=input()
print(type(entrada))
#Busca si un numero es entero o no
esEntero=(entrada.isdigit() and entrada.find(".")==-1 )
#creamos una condicion, donde si esEntero es es entero, mostrara el mensaje
if(esEntero):
    print("Dato entero. !muy bien!")
    #si no es entero mostrara el siguiente mensaje
else:
    print("Dato no es entero. Intentar nuevamente")