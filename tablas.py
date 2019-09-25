for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(1))

    print()
    for j in range(1,11):
        #I es el numero de la tabla
        #y j el elemento
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #se hace un salto de linea cuando se hagan las iteraciones
        print()