Cantantes = ['milo j', 'bad bunny', 'taylor swift', 'bruno mars']
Musicas = ['Tus Vueltas', 'Baile Inolvidable', 'Shake It Off', 'Risk It All']
Duración = ['3.30','2.15','3.19','4.32']

print(Cantantes)
while True:
    eleccion = input("Cual artista te gustaria escuchar chaval?").lower()
    if eleccion == 'taylor swift':
        print('Agh... que mierda de artista mejor vete a leer.')
        nseq = input("Estas seguro/a de que quieres escuchar esta mierda?").lower()
        if nseq == 'si':
            print("Agh...")
            indice = Cantantes.index(eleccion)
            print("======REPRODUCIENDO======", Musicas[indice], Duración[indice],'min')
            break
    elif eleccion in Cantantes:
        indice = Cantantes.index(eleccion)
        print(eleccion , 'tiene esta canción:', Musicas[indice], 'con una duración de', Duración[indice])
        nose = input("La quieres escuchar?").lower()
        if nose == 'si':
            print("======REPRODUCIENDO======", Musicas[indice], Duración[indice],'min')
            break
        else:
            print("Ok chaval, empecemos de cero.")
            continue
    else:
        print("Artista no encontrado intenta denuevo")
        continue
    
