def leer_horas_tarifa():
    horas = float(input("Ingrese el número de horas trabajadas: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))
    return horas, tarifa

def calcular_pago(horas, tarifa):
    return horas * tarifa

def mostrar_pago(pago):
    print("El pago semanal es:", pago)
