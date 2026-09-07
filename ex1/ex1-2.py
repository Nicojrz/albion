import random
def ruleta(poblacion, aptitud)
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    aptitudTotal = sum(aptitudes)

    probabilidades = [aptitud/aptitudTotal for aptitud in aptitudes]

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
