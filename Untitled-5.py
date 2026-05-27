colores = ("Rojo", "Verde")

lista_temporal = list(colores)

lista_temporal[0] = "Azul"

colores = tuple(lista_temporal)
print(f"Tupla final modificada: {colores}")