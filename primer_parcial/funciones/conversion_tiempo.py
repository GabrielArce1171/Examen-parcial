def leer_segundos(segundos):
    segundos = int(input("Ingrese el número de segundos: "))
    return segundos

def convertir_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def mostrar_tiempo(horas, minutos, segundos):
    print(f"Tiempo convertido: {horas} horas, {minutos} minutos, {segundos} segundos")