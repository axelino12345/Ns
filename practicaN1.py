intentos = 3

while intentos > 0:
    usuario = input("Quien eres?")
    contraseña = input("Cual es tu contraseña?")

    if usuario == 'alvaro' and contraseña == '1234':
        print('Bienvenido', usuario)
        intentos = 0


    else:
        print('Credenciales incorrectas')
        intentos -= 1


    if intentos == 0:
        print('Has agotado tus intentos, vuelve a intentarlo mas tarde')
