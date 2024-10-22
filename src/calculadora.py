class NoSePuedeCalcular(Exception):
    pass

# src/calculadora.py
def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía")
    return elementos[0] if len(elementos) == 1 else sum(elementos) / len(elementos)
