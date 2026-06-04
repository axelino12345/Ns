intentos = 3
usuarios = ['alvaro', 'maria', 'juan']
contraseñas = ['1234', '12345', 'abcd']

while intentos > 0:
    entrada = input('Quien eres? ')
    entrada2 = input('Cual es tu contraseña? ')

    if entrada in usuarios:
        indice = usuarios.index(entrada)
        if contraseñas[indice] == entrada2:
            print('hola', entrada)
            break

    print('Credenciales incorrectas, intente de nuevo')
    intentos -= 1

if intentos == 0:
    print('Has agotado tus intentos, vuelve a intentarlo más tarde')