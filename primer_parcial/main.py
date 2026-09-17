import funciones.conversion_tiempo as conversion_tiempo
import funciones.pago_semanal as pago_semanal
import funciones.triangulo as triangulo

def main():
    triangulo.leer_base_altura()
    triangulo.leer_calcular_area()
    triangulo.mostrar_area()

    leer_horas_tarifa()
    calcular_pago()
    mostrar_pago()

    conversion_timepo.leer_segundos()
    conversion_timepo.convertir_tiempo()
    conversion_timepo.mostrar_tiempo()

    def main(): 
pass 
if __name__ == "__main__": 
main() 