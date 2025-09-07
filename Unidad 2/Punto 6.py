import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100)for i in range(50)]
mean_mio = mean (numeros_aleatorios)
mode_mio = mode (numeros_aleatorios)
median_mio = median (numeros_aleatorios)
if mean_mio > median_mio and median_mio > mode_mio:
    print ("Sesgo positivo")
if mean_mio < median_mio and median_mio < mode_mio:
    print ("Sesgo negativo")
if mean_mio == median_mio and mean_mio == mode_mio and median_mio == mean_mio and median_mio == mode_mio and mode_mio == mean_mio and mode_mio == median_mio:
    print ("Sin sesgo")
