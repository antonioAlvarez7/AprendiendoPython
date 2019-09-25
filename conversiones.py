# creamos una variable de tipo string
numero = "1234"
#Mostramos de que tipo es la variable numero
print(type(numero))
#Convertimos la variable a tipo entero
numero = int (numero)
#Mostramos el nuevo tipo de vartiable de la variable numero
print(type(numero))

salida = "el numero utilizado es {}"

print(salida.format(numero))