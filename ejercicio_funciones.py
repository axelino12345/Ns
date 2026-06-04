#crear una función que convierta horas a minutos..


def convertir_horas(horas):
    minutos = 60
    conv_minutos = horas * minutos
    return conv_minutos

print(convertir_horas(10))



#crear una función que calcule el precio final de un juego cuando tiene rebajas.


def calcular_descuento(precio_orig, porcentaje):

    precio_final = precio_orig * (porcentaje / 100)

    return precio_orig - precio_final

print(calcular_descuento(50, 20))




#nsq detector de lag


def control_rendimiento(fps):
   if fps >= 60:
       return ("Tu pc anda joya crack")
   else:
       return ("Tu pc de cartón está sufriendo, cambia de juego crack")


print(control_rendimiento(700))


#nsq mas


def calcular_tiempototal(horas2, mins_extras):

    tiemposs = horas2 * 60

    return tiemposs + mins_extras

print(calcular_tiempototal(10, 45))
