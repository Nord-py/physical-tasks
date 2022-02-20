import matplotlib.pyplot as plt
import numpy as np
from math import sin, sqrt, cos, pi, e

fig, ax = plt.subplots()

Amp = 1 # Амлитуда
Len = 100 # длина нити
n = 5 # Номер гармоники

while n <= 5: # Тут можно указать количество гармоник на графике
    y_m = []
    x_m = []

    for x in range(0, Len):
        y = Amp * sin(pi * n * x / Len)
        x_m.append(x)
        y_m.append(y)
        grid1 = plt.grid(True)
        plt.plot(x_m, y_m, linewidth=4)
    n += 1
plt.show()

