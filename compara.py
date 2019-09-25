#se piden 2 numeros
numero1 = input("numero1:")
numero2 = input("numero2:")
salida ="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #si los numeros son iguales, muestra el mensaje
    print(salida.format(numero1,numero2,"Los numeros son iguales")) 
else:
    #si no los son, entra a este if dentro de otro if
    if numero1 > numero2:
        #si el mayor es primero muestra el sig mensaje
        print(salida.format(numero1,numero2,"El mayor es primero"))

    else:
        #sino muestra:
         print(salida.format(numero1,numero2,"El mayor es el segundo"))
