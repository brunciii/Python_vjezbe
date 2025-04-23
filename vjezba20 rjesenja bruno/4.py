def jedistveni_elementi(lista):
    for element in lista:
        if lista.count(element) > 1:
            lista.remove(element)


    return lista
    
