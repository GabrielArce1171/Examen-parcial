def leer_base_altura():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura

def calcular_area(base, altura):
    return (base * altura) / 2

def mostrar_area(area):
    print("El área del triángulo es:", area)