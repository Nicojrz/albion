import random

import matplotlib.pyplot as plt

def ruleta(poblacion, aptitud):
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    aptitud_total = sum(aptitudes)
    aleatorio = random.uniform(0, aptitud_total)

    acumulado = 0
    for indice, aptitud_individuo in enumerate(aptitudes):
        acumulado += aptitud_individuo
        if aleatorio <= acumulado:
            return indice


def torneo(poblacion, tam, aptitud):
    indices = random.sample(range(len(poblacion)), tam)
    return max(indices, key=lambda indice: aptitud(poblacion[indice]))


TAM_POBLACION = 100
NUM_PRUEBAS = 10_000
TAM_TORNEO = 2

# La semilla permite reproducir la misma población y la misma prueba.
random.seed(42)
POBLACION = [
    [random.uniform(0, 10), random.uniform(0, 10)]
    for _ in range(TAM_POBLACION)
]
APTITUD = lambda individuo: sum(individuo)

conteos_torneo = [0] * TAM_POBLACION
conteos_ruleta = [0] * TAM_POBLACION

for _ in range(NUM_PRUEBAS):
    conteos_torneo[torneo(POBLACION, TAM_TORNEO, APTITUD)] += 1
    conteos_ruleta[ruleta(POBLACION, APTITUD)] += 1

orden = sorted(range(TAM_POBLACION), key=lambda indice: APTITUD(POBLACION[indice]))
aptitudes_ordenadas = [APTITUD(POBLACION[indice]) for indice in orden]
torneo_ordenado = [conteos_torneo[indice] for indice in orden]
ruleta_ordenada = [conteos_ruleta[indice] for indice in orden]

NUM_RANGOS = 10
limite_inferior = 0
limite_superior = 20
ancho_rango = (limite_superior - limite_inferior) / NUM_RANGOS
limites_bins = [
    limite_inferior + indice * ancho_rango
    for indice in range(NUM_RANGOS + 1)
]

plt.figure(figsize=(12, 6))
plt.hist(
    [aptitudes_ordenadas, aptitudes_ordenadas],
    bins=limites_bins,
    weights=[torneo_ordenado, ruleta_ordenada],
    label=['Torneo binario', 'Selección por ruleta'],
    alpha=0.65,
    edgecolor='black',
)
plt.xlabel('Rangos de aptitud')
plt.ylabel('Frecuencia: número de selecciones')
plt.title(f'Histograma de frecuencias en {NUM_PRUEBAS:,} pruebas')
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
