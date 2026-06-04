import time

while True:
    print("Que operación necesitas hacer?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raiz cuadrada")

    opcion = input("Selecciona una opción 1-5")

    if opcion == "1":
        numero1 = int(input("Ingresa el primer valor(a)"))
        numero2 = int(input("Ingresa el segundo valor(b)"))
        resultado1 = numero1 + numero2
        print(f"Este es el resultado {resultado1}")
        time.sleep(2)
        pass
    elif opcion == "2":
        numeroz = int(input("Ingresa el primer valor(a)"))
        numerox = int(input("Ingresa el segundo valor(b)"))
        resultadoz = numeroz - numerox
        print(f"Este es el resultado {resultadoz}")
        time.sleep(2)
        pass
    elif opcion == "3":
        numerov = int(input("Ingresa el primer valor(a)"))
        numeroe = int(input("Ingresa el segundo valor(b)"))
        resultadof = numerov * numeroe
        print(f"Este es el resultado {resultadof}")
        time.sleep(2)
        pass

    elif opcion == "4":
        numero4 = int(input("Ingresa el primer valor(a)"))
        numero5 = int(input("Ingresa el segundo valor(b)"))
        resultadot = numero4 / numero5
        print(f"Este es el resultado {resultadot}")
        time.sleep(2)
        pass

    elif opcion == "5":
        numeron = int(input("Ingresa el número deseado"))

        resultadoxc = numeron**0.5
        print(f"Este es el resultado {resultadoxc}")
        time.sleep(2)
        pass

    else:
        print("Opción inválida, intenta de nuevo")
        time.sleep(2)
