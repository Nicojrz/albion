import random

def torneo(poblacion, tam, aptitud):
    seleccion = random.sample(poblacion, tam)
    print(seleccion)
    ganador = max(seleccion, key = aptitud)
    return ganador

POBLACION = [[5.0, 2.3], [7.2, 4.6], [2.5, 6.8],
             [12.0,4.8], [1.9, 1.0], [5.1, 7.2]]
TAM = 3
APTITUD = lambda x : sum(x)

individuo = torneo(POBLACION, TAM, APTITUD)
print('indiviudo seleccionado:', individuo)
