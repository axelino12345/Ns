import time  # Tenés que importar la librería al principio de todo

print("El sistema se va a bloquear por seguridad...")
segundos = 5

while segundos > 0:
    print(f"Desbloqueo en: {segundos} segundos...")
    time.sleep(1)  # El programa se frena acá por 1 segundo
    segundos -= 1  # Le restamos 1 al contador

print("¡Listo! Podés intentar de nuevo.")
