class NoSePuedeCalcular(Exception):
    pass

def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía")
    return sum(elementos) / len(elementos)

