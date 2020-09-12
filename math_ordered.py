'''
    Ignacio Saccomano 2020

    Este programa busca ordenar los ejercicios de una guía y decirle al usuario cuántos le falta hacer en caso de que así sea.
    Todo esto con tan solo introducir los ejercicios hechos uno por uno.
'''

ejercicios = []     # Creo lista de todos los ejercicios que hizo el usuario
total = []         # Lista del total de los ejercicios presentes en la guía para luego comparar con lo que hizo el usuario.


many = int(input("Cuántos ejercicios son? "))   # Tamaño de la lista de los ejercicios totales.

def bad_luck(n):
        num = len(ejercicios)
        div = many
        stat = num / div

        if stat == 0:
            return "100"
        else:
            for i in range(n - 1):
                stat *= (num - 1) / (div - 1)
        return str(round(100 - stat * 100))

while True:
    try:
        data = int(input("Ejercicio: "))        # El usuario pone los ejercicios que hace y apreta enter. Cuando termina apreta enter sin poner nada.
    except:
        break
    ejercicios.append(data) # Se agrega a la lista de los ejercicios lo que pone el usuario

ejercicios = list(dict.fromkeys(ejercicios)) # En caso de que haya puesto 2 veces lo mismo, acá se corrige.

print("Estos son los ejercicios que hiciste en orden: " + str(sorted(ejercicios)))  # Se muestran los ejercicios hechos en orden.

if len(ejercicios) == many:     # Se verifica si el usuario termino de hacer los ejercicios o no.
    print("Felicidades, ya terminaste el TP ;) \nAhora a disfrutar")
else:
    for i in range(many):
        total.append(i + 1)    # Se crea una lista con el total de los ejercicios de la guía para deducir cuántos y cuáles faltan

    missing = many - len(ejercicios)

    restantes = list(set(total) - set(ejercicios))  # Lista de los ejercicios que le quedan por hacer

    done = (len(ejercicios)/many) * 100   # Porcentaje de la guía hecha.

    print("Te faltan hacer " + str(missing) + " ejercicios.")
    print("\nEsos ejercicios son: " + str(sorted(restantes)))
    print("Hiciste el " + str(int(done)) + "% de la guía.")

    luck = int(input("Cuántos ejercicios va a pedir? "))

    print("La probabilidad de que te pida algo que no hayas hecho es del " + bad_luck(luck) + "%")   # Probabilidad de que te pida un ejercicio que no hiciste.
    # IDEA: Agregar función que calcule la probabilidad de que te pida un ejercicio que no hayas hecho.
