def izdvoji_parne(lista_brojeva):
    parni = []
    for broj in lista_brojeva:
        if broj % 2 == 0:
            parni.append(broj)
    return parni


print(izdvoji_parne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))