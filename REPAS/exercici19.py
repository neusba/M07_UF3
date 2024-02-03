# Cal buscar la informació que es demana de la següent list:
# areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]

areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# Imprimir el segon element
print(areas_pis[1:2])

# Imprimir l’últim element
print(areas_pis[-1:])

# Imprimir l’àrea de la terrassa
print(areas_pis[areas_pis.index("Terrassa")+1: areas_pis.index("Terrassa")+2])

# Imprimir del primer element al tercer element
print(areas_pis[0:3])

# Imprimir del tercer element a l’últim
print(areas_pis[2:])

# Imprimir el total de l'àrea de les dues habitacions
print(areas_pis[areas_pis.index("Habitació1") + 1] + areas_pis[areas_pis.index("Habitació2") + 1])

# Modificar l’àrea del lavabo i imprimir la nova list area
areas_pis[areas_pis.index("Lavabo") + 1] = 10
print(areas_pis)

# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
areas_pis.extend(["Pati interior", 2.78])
print(areas_pis)

# Imprimir el total de l’àrea del pis.
print('El total del area del piso es:', areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13] + areas_pis[15])
