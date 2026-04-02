# Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

hotel = {
    "name" : "Hotel California",
    "number_of_stars" : 5,
    "rooms" : [
        {
            "number" : 101,
            "floor" : 1,
            "price_per_night" : 100
        },
        {
            "number" : 102,
            "floor" : 1,
            "price_per_night" : 150
        },
        {
            "number" : 201,
            "floor" : 2,
            "price_per_night" : 200
        }
    ]
}
print(hotel)
