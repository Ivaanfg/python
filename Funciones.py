def media(lista):
    suma = sum(lista)
    med = suma / len(lista)
    return med


def solicitar_datos():
    nombres = []
    alturas = []
    pesos = []
    var = 0
    personas = int(input("Introduce el numero de personas que quieres introducir:"))
    while var != personas:
        nom = input("Introduce el nombre:")
        alt = float(input("Introduce la altura:"))
        peso = float(input("Introudce tu peso ;):"))
        alturas.append(alt)
        nombres.append(nom)
        pesos.append(peso)
        var += 1
    x = media(alturas)
    p = media(pesos)
    return nombres, alturas, pesos, p, x


def fecha():
    from datetime import datetime
    import re
    patron = re.compile(".{2}/.{2}/.{4} .{2}:.{2}$")
    data = input("Introduce una fecha:")
    if patron.match(data):
        dat = datetime.strptime(data, "%d%m%Y% %H%M")
    return dat


def clase():
    diccionario = {}
    x, y, p, l, z = solicitar_datos()
    for i in range(len(x)):
        diccionario.setdefault(x[i], [y[i], p[i]])
        date = fecha()
    return diccionario, "Media peso:", z, "Media altura:", l, "La fecha introducida es:", date


