#se crea un valor entero y un string, que de momento no tienen ningun valor
acumulado = int(0)
numero = str("")

while True:
    numero = input("Dame un numero entero: ")
    if numero == "":
        #si se deja el campo vacio, sale del programa
        print("Vacio. Salida del programa. ")
        break
    else:
        #sino muestra lo siguiente
        acumulado +=int(numero)
        salida = "Monto acumulado: {}"
        print(salida.format(acumulado))
