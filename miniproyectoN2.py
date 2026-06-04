juegos = ['Subnautica', 'Minecraft', 'Hollow Knight']
precios = [15, 10, 20]
while True:
    try:
        billetera = int(input("Cuanto dinero traes chaval?"))
        
        if billetera > 1000:
            print("Ni tu te crees que tienes tanto dinero, dime la verdad.")
            continue
        break
    except ValueError:
        print("Eso no es un número chaval, intenta denuevo.")
if billetera < 10:
    print("No te da ni para un caramelo chaval vuelve cuando tengas dinero, pobre.")
else:
    while billetera >= 10:
        print(juegos)
        entrada = input('Estos son los juegos disponibles cual quieres comprar?')
        if entrada in juegos:
            indice = juegos.index(entrada)
            print("este juego cuesta", precios[indice], 'dolares')
            comprar_juego = input("Quieres comprarlo?")
            if comprar_juego == 'si':
                billetera -= precios[indice]
                print('Compraste', entrada , 'felicidades!')
                print("te quedan" ,billetera , "dolares")
        else:
            print("Juego no encontrado, intenta denuevo")

    
