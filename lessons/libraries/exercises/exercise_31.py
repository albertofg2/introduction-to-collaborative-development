from numpy import sin, pi
from scipy import quad
import time


a, b = 0, pi/2

# Por suma de Rieman
start_time=time.perf_counter()
n=1000
△ x  =(b-a)/n
integral_rieman=(∑ i = 1 n f ( x i ∗ )△ x )
time_rieman=time.perf_counter()-start_time

# Por scipy
start_time=time.perf_counter()
scipy_integral, scipy_error = quad(a,b)
time_scipy=time.perf_counter()-start_time

# Resultados
print('El tiempo de Rieman ha sido de',time_rieman)
print('El tiempo de Rieman ha sido de',time_scipy)
print('La diferencia de tiempos ha sido de',rieman_time-time_scipy)
