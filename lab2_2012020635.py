import numpy as np
import time


# inicia el tiempo de ejecucion
start_time = time.time()

# Al usar numpy.random.normal,
# puede pasar argumentos de palabras
# clave para establecer la desviacion media
# y estandar de su matriz devuelta.
# Estos argumentos de palabras clave son loc (mean)
# y escala (std).
# instanciamos la cantidad de datos que se requiere
N = 10000000
# media
mean = 500
# escala
std = 30
# array que tendra todos los puntos
puntos_de_distribucion = []

# iniciar contador de puntos menores a 500000
result = 0

while len(puntos_de_distribucion) < N:
    y = np.random.normal(loc=mean, scale=std, size=1)[0]
    # llenar el array de source de los puntos de distribucion
    puntos_de_distribucion.append(y)
    # verificar que el numero sea menor a 50000
    if y < 500:
        result += y

# termina el tiempo de ejecucion

print("--- %s seconds ---" % (time.time() - start_time))
print("--- suma total: ", result)
