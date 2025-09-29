# Practica 1 - Algoritmos Bioinspirados
# Cornejo Morales Paola
# Hernández Martínez Ernesto Ulises

import random

#   Vamos a abordar de problema de la mochila para el mundo de Harry Potter
#       Hay 10 productos de cada tipo
#       Capacidad de la mochila : 30 lb
max_capacity = 30
#   Restricciones
#       Al menos 3 'Love Potion'
#       Al menos 2 'Skiving Snackbox'

#   Poblacion
#       10 cromosomas
cpoblacion = 10
#   Generaciones
#       50 generaciones
max_generations = 50
#   Probabilidad de cruza
#       0.85
#   Probabilidad de mutación
#       0.1
#   Selección de padres
#       Ruleta
#   Método de cruza
#       Cruza uniforme (u =< 0.5)
#   Método de mutación
#       Mutación uniforme
#   Selección de sobrevivientes
#       Generación con reemplazo del padre más debil

#   PRODUCTOS
#       Decoy Detonators            (0)     1
#           Weight: 4 lb
#           Price: $ 10
#       Love Potion                 (1)     2
#           Weight: 2 lb
#           Price: $ 8
#       Extendable Ears             (2)     3
#           Weight: 5 lb
#           Price: $ 12
#       Skiving Snackbox            (3)     4
#           Weight: 5 lb
#           Price: $ 6
#       Fever Fudge                 (4)     5
#           Weight: 2 lb
#           Price: $ 3
#       Puking Pastilles            (5)     6
#           Weight: 1.5 lb
#           Price: $ 2
#       Nosebleed Nougat            (6)     7
#           Weight: 1 lb
#           Price: $ 2

weights = [4, 2, 5, 2, 1.5, 1]
prices =  [10, 8, 12, 6, 3, 2]

# Nuestros individuos serán cadenas Int de longitud 7
#     ej.   [0-10][0-10][0-10][0-10][0-10][0-10][0-10]

def create_generation():
    new_generation = []

    for i in range(cpoblacion) :
        individual = []
        while True:
            individual = [random.randint(0, 10) for j in range(7)]

            if individual[1] < 3:  # Love Potions index 1
                individual[1] = random.randint(3, 10)
            if individual[3] < 2:  # Snackbox index 3
                individual[3] = random.randint(2, 10)

            w, v = fitness(individual)
            if w <= max_capacity:
                break

        new_generation.append(individual)

    return new_generation

def fitness(individual):
    t_weight = sum(individual[i] * weights[i] for i in range(len(weights)))
    t_value = sum(individual[i] * prices[i] for i in range(len(prices)))
    return t_weight, t_value

new_generation = create_generation()

# to print the generation
for i in range(cpoblacion):
    w, v = fitness(new_generation[i])
    print("Individuo ", i,": ", new_generation[i], "Total weight: ", w, "Total value: ", v)
