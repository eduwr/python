def imprimir(maximo, atual):
    if atual < maximo:    #condição de parada
        print(atual)
        imprimir(maximo, atual + 1)

imprimir(10, 1)