#se pide un numero entero
numero = int(input("Dae un numero entero: "))
#si el residuo es 0, quiere decir que es multiplo
esMultiplo3 = ((numero%3)==0)
esMultiplo5 = ((numero%5)==0)
esMultiplo7 = ((numero%7)==0)
#si es multiplo de 3 y de 5, o de 7
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    #sino
    print("Incorrecto.")
