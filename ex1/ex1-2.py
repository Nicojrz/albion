import random

def ruleta(poblacion, aptitud):
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    aptitudTotal = sum(aptitudes)

    probabilidades = [aptitudIndiv/aptitudTotal for aptitudIndiv in aptitudes]

    print('individuos: ', poblacion)
    print('aptitudes: ', aptitudes)
    print('probabilidades: ', probabilidades)

    aleatorio = random.random()
    print('numero aleatorio entre 0 y 1: ', aleatorio)

    acumulado = 0

    for i, probabilidad in enumerate(probabilidades):
        acumulado += probabilidad
        if aleatorio <= acumulado:
            return poblacion[i]

POBLACION = [[5.0, 2.3], [7.2, 4.6], [2.5, 6.8],
             [12.0,4.8], [1.9, 1.0], [5.1, 7.2]]
APTITUD = lambda x : sum(x)

individuo = ruleta(POBLACION, APTITUD)
print('indiviudo seleccionado:', individuo)
