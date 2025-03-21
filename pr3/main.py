import pandas as pd
import time
import matplotlib.pyplot as plt
from numba import jit

file_name = 'generated_sensor_data.csv'
data = pd.read_csv(file_name)

power = data['Power_W'].values
temp = data['Temperature_C'].values
factor = data['Factor'].values

def energy_needs(power, temp, factor):
    energy = 0
    for p, t, f in zip(power, temp, factor):
        energy += (p * (1 + t / 100) * f)
    return energy

@jit(nopython=True)
def energy_needs_numba(power, temp, factor):
    energy = 0.0
    for i in range(len(power)):
        energy += power[i] * (1 + temp[i] / 100) * factor[i]
    return energy

start = time.time()
energy_python = energy_needs(power, temp, factor)
python_time = time.time() - start

start = time.time()
energy_numba = energy_needs_numba(power, temp, factor)
numba_time = time.time() - start

print(f"Енергетичні потреби (Python): {energy_python:.2f}, Час: {python_time:.6f} сек")
print(f"Енергетичні потреби (Numba): {energy_numba:.2f}, Час: {numba_time:.6f} сек")

# Побудова графіку
labels = ['Python', 'Numba']
times = [python_time, numba_time]
plt.bar(labels, times, color=['red', 'green'])
plt.ylabel('Час виконання (сек)')
plt.title('Порівняння продуктивності: Python vs Numba')
plt.show()

# Numba справляється краще