from scipy.stats import truncnorm
import numpy as np
import time


# inicia el tiempo de ejecucion
start_time = time.time()

# esta funcion genera los puntos dentro del rango requerido
# y utilizando la media y escala requerida hacemos uso del import truncnorm

# genera el punto


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


# intancia la funcion para su uso
X = get_truncated_normal(mean=500, sd=30, low=0, upp=500)
# generamos los 10 millones de puntos de distribucion con la escala requerida y la media de igual forma
points = X.rvs(10000000)
a = np.array(points)


def menor(numero):    # Primero declaramos una funcion condicional
    if numero < 500:  # Comprobamos si un numero es multiple de cinco
        return True


r = filter(menor, a)
# print(r)
result = sum(r)

# result = sum(x < 500 for x in a)
# termina el tiempo de ejecucion
print("--- %s seconds ---" % (time.time() - start_time))
print("--- suma total: ", result)
