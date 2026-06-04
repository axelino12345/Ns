import time

bolsillo = 500
saldo = 1000
pinc = "1234"
caramelos = 2
historial = ["Apertura de la cuenta: +$1000"]
online = False
while True:
    if not online:
        print("=== BIENVENIDO AL CAJERO AUTOMÁTICO ===")
        print("Inserte su targeta")
        targeta = input("Insertar targeta?\n    =======SI/NO=======").lower()
        if targeta == "si":
            print("Targeta insertada correctamente")
            time.sleep(2)
            pin = input("Ingrese su PIN: ")
            if pin == pinc:
                print("PIN correcto")
                online = True
                time.sleep(2)
            else:
                print("PIN incorrecto")
                time.sleep(4)
                continue

        else:
            print("No se pudo insertar la targeta")
            continue

    print("¿Qué deseas hacer chaval?")
    print("1. Ver saldo")
    print("2. Mirar el bolsillo")
    print("3. Retirar dinero")
    print("4. Depositar dinero")
    print("5. Ver historial de movimientos")
    print("6. Comer un caramelo")
    print("7. Salir")

    opcion = input("Selecciona una opción (1-7): ")

    if opcion == "1":
        print(f"===TIENES {saldo} PESOS===")
        time.sleep(2)
        pass

    elif opcion == "2":
        print(f"${bolsillo} pesos y {caramelos} caramelos")
        time.sleep(3)

    elif opcion == "3":
        retiro = int(input("Cuanto dinero quieres retirar?"))
        if retiro > saldo:
            print("Saldo insuficiente.")
            time.sleep(2)

        else:
            saldo -= retiro
            historial.append(f"-${retiro}")
            bolsillo += retiro
            print(
                f"Has retirado exitosamente ${retiro} pesos de la cuenta, te quedan ${saldo} pesos disponibles"
            )
            time.sleep(3)
        pass

    elif opcion == "4":
        deposito = int(input("Cuanto quieres depositar a la cuenta?"))
        if deposito > bolsillo:
            print("No tienes dinero suficiente para depositar")
            time.sleep(2)
            pass

        else:
            saldo += deposito
            bolsillo -= deposito
            historial.append(f"+${deposito}")
            print("Deposito hecho con exito.")
            time.sleep(2)

        pass

    elif opcion == "5":
        print(historial)
        time.sleep(4)
        pass

    elif opcion == "6":
        segundos = 3
        if caramelos > 0:
            caramelos -= 1
            print("Comiste un caramelo...")
            while segundos > 0:
                print("...")
                time.sleep(1)
                segundos -= 1
            print("Sabe horrible")
            time.sleep(3)
            pass

        else:
            print("Te quedaste sin caramelos")
            time.sleep(2)
            pass

    elif opcion == "7":
        print("Gracias por usar el cajero. Nos vemos!")

        segs = 4
        while segs > 0:
            print("Esperando nuevo usuario.")
            time.sleep(1)
            segs -= 1
        online = False

    else:
        print("Opción inválida, intenta de nuevo.")
