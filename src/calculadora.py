class NoSePuedeCalcular(Exception):
    pass

def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía")
    return 0 if all(e == 0 for e in elementos) else sum(elementos) / len(elementos)

