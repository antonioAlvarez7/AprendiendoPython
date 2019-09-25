#Pide un numero que despues se convierte a entero
numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
#se crea un iteracion con rango de 1 a 11 
for i in range(1,11):
    #i va variando en cada iteracion
    salida ="{} x {} = {}"
    print(salida.format(numero,i,i*numero))