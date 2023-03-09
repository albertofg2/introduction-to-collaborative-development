import numpy as np
from scipy import integrate
import time

a, b = 0,np.pi/2

# Por suma de Riemann
start_time = time.perf_counter()
n = 10000
dx = (b-a)/n
x=np.arange(a,b,dx)
riemann_integral = sum(np.sin(x)*dx)
time_riemann = time.perf_counter()-start_time

# Integral por scypi
start_time = time.perf_counter()
scipy_integral, scipy_error = integrate.quad(np.sin, a, b)
time_scipy = time.perf_counter()-start_time

# Resultados
print('La integral por Riemann es:', riemann_integral)
print('La integral por Scipy es:', scipy_integral)
print('El tiempo de Riemann ha sido de', time_riemann)
print('El tiempo de Scipy ha sido de', time_scipy)
print('La diferencia de tiempos ha sido de', time_riemann-time_scipy)
