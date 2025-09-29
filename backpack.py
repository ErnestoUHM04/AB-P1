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
p_cruza = 0.85
#   Probabilidad de mutación
#       0.1
p_muta = 0.1
#   Selección de padres
#       Ruleta
#   Método de cruza
#       Cruza uniforme (u =< 0.5)
u = 0.5
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

weights = [4, 2, 5, 5, 2, 1.5, 1]
prices =  [10, 8, 12, 6, 3, 2, 2]
best_individuals = []

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

def print_generation(new_generation, cpoblacion = cpoblacion):
    # to print the generation
    for i in range(cpoblacion):
        w, v = fitness(new_generation[i])
        print("Individuo ", i,": ", new_generation[i], "Total weight: ", w, "Total value: ", v)

def get_p_a(new_generation):
    #ruleta para la seleccion de individuos para cruza
    v_sum = 0
    values = []
    for i in range(cpoblacion):
        w, v = fitness(new_generation[i])
        values.append(v)
        v_sum += v
    #print(values)
    #print(v_sum)
    #p_values = []
    p_a_values = []
    p_a_v = 0
    for i in range(len(values)):
        p_v = values[i] / v_sum
        #p_values.append(p_v)
        p_a_v += p_v
        p_a_values.append(p_a_v)
    #print(p_values)
    #print(p_a_values)
    return p_a_values

def roulette(p_a_values):
    roulette = random.random() # random number in between 0 and 1
    #print("roulette", roulette)

    selected_individual = None

    for i in range(cpoblacion):
        if roulette <= p_a_values[i]:
            selected_individual = new_generation[i]
            break

    #print(selected_individual)
    return selected_individual

def cruza_uniforme(Father1, Father2):
    # dont remember about this one
    l = len(Father1)

    Son1 = []
    Son2 = []

    s_aux = []
    for i in range(l):
        s = random.random() # a random number from 0 to 1
        s_aux.append(s)
    #print(s_aux)
    for i in range(l):
        if s_aux[i] < u:
            Son1.append(Father1[i])
            Son2.append(Father2[i])
        else:
            Son1.append(Father2[i])
            Son2.append(Father1[i])

    return Son1, Son2

def muta(Son1, Son2):
    while True:
        for i in range(len(Son1)):
            m = random.random()
            if m < p_muta: # we modify this gene
                Son1[i] = random.randint(0,10)
            if Son1[1] < 3:  # Love Potions index 1
                Son1[1] = random.randint(3, 10)
            if Son1[3] < 2:  # Snackbox index 3
                Son1[3] = random.randint(2, 10)
        # Once we go over all of this, we check if it still is in the restrictions
        w, v = fitness(Son1)
        if w <= max_capacity:
            break

    while True:
        for i in range(len(Son2)):
            m = random.random()
            if m < p_muta:
                Son2[i] = random.randint(0,10)
            if Son2[1] < 3:  # Love Potions index 1
                Son2[1] = random.randint(3, 10)
            if Son2[3] < 2:  # Snackbox index 3
                Son2[3] = random.randint(2, 10)
        w, v = fitness(Son2)
        if w <= max_capacity:
            break

    return Son1, Son2

def create_next_generation(new_generation):
    next_generation = [] # next gen
    next_gen_p = 0 # this is the counter for the next generation
    p_a_values = get_p_a(new_generation)

    while True:
        #after we got the accumulated probabilities, we can get spin the roulette
        Father1 = roulette(p_a_values)

        while True:
            Father2 = roulette(p_a_values)
            if Father2 != Father1:
                break

        #print("Father 1: ",Father1)
        #print("Father 2: ",Father2)
        # once we get both fathers, we use 'p_cruza' to roll the dice and know if they are going to reproduce
        reproduce = random.random()
        #print(reproduce)

        if reproduce < p_cruza:
            # then we reproduce both individuals
            Son1, Son2 = cruza_uniforme(Father1, Father2)
            # after this, we still have to mutate each child
            #print("Sons:", Son1, Son2)
            Son1, Son2 = muta(Son1, Son2)
            #print("Sons:", Son1, Son2)
            # now ge add this 2 new individuals into the new gen
            ####################################################
            # we now have to run a mini tournament (both parents and both sons) to get the best 2 individuals
            Best1, Best2 = mini_tournament(Father1, Father2, Son1, Son2)
            next_generation.append(Best1)
            next_generation.append(Best2)
            next_gen_p += 2
        else:
            # they go directly to the new generation of individuals
            next_generation.append(Father1)
            next_generation.append(Father2)
            next_gen_p += 2 # if this happends, we got 2 new individuals into the new gen

        if next_gen_p >= cpoblacion:
            break

    return next_generation

def find_best_i(new_generation):
    best_i = None
    best_value = 0

    for i in range(cpoblacion):
        w, v = fitness(new_generation[i])
        if best_i == None or v > best_value:
            best_value = v
            best_i = new_generation[i]
    print(best_i) # nice

    return best_i

def mini_tournament(Father1, Father2, Son1, Son2):
    players = [Father1, Father2, Son1, Son2]

    fitness_list = []
    for i in range(len(players)):
        w, v = fitness(players[i])
        fitness_list.append((players[i],v))
    #print(fitness_list)

    fitness_list.sort(key=lambda x: x[1], reverse=True)

    Best1 = fitness_list[0][0]
    Best2 = fitness_list[1][0]

    return Best1, Best2

print("\tInital generation")
new_generation = create_generation()
print_generation(new_generation)

best_i = find_best_i(new_generation)
best_individuals.append(best_i)

generation_number = 0
while True:
    generation_number +=1
    new_generation = create_next_generation(new_generation)
    print("\nNext generation", generation_number)
    print_generation(new_generation)
    best_i = find_best_i(new_generation)
    best_individuals.append(best_i)
    if generation_number >= max_generations:
        break

print("\n\tBest Individuals")
print_generation(best_individuals, len(best_individuals))