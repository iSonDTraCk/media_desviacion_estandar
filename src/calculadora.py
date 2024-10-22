class NoSePuedeCalcular(Exception):
    pass

def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía")
    if not all(isinstance(e, (int, float)) for e in elementos):
        raise TypeError("Todos los elementos deben ser números")
    return sum(elementos) / len(elementos)


