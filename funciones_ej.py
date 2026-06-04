def pasar_a_pesos(precio_dolares):
    tipo_cambio = 43  # Precio del dólar hoy
    precio_final = precio_dolares * tipo_cambio
    return precio_final

# Ahora la usás para cualquier juego que mires:
juego1 = pasar_a_pesos(15)
juego2 = pasar_a_pesos(60)
juego3 = pasar_a_pesos(4.5)

print(f"El primer juego cuesta ${juego3} pesos.")
