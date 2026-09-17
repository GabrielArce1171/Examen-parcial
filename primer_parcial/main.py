import funciones.triangulo as triangulo
import funciones.pago_semanal as pago_semanal
import funciones.conversion_tiempo as conversion_tiempo

def main():
    base, altura = triangulo.leer_base_altura()
    area = triangulo.calcular_area(base, altura)
    triangulo.mostrar_area(area)

    horas, tarifa = pago_semanal.leer_horas_tarifa()
    pago = pago_semanal.calcular_pago(horas, tarifa)
    pago_semanal.mostrar_pago(pago)

    segundos = conversion_tiempo.leer_segundos()
    horas, minutos, segundos = conversion_tiempo.convertir_tiempo(segundos)
    conversion_tiempo.mostrar_tiempo(horas, minutos, segundos)

 def main(): 
pass 
if __name__ == "__main__": 
main()