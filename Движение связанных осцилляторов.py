from math import cos, sqrt
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

A_1 = 1 # амплитуда колебаний (Ф)
A_2 = 1
f_0_1 = 10 # Начальная фаза
f_0_2 = 1
L = 15 # Длина нити
L_1 = 5 # Длина нити на котором крепется пружина
g = 9.81 # УСП
m = 2 # Масса груза - будет одинаковой у обоих
k = 1 # Коэф. упругости нити
t = 0 # Время

w_0 = sqrt(L / g)
x = sqrt( (k * L_1**2) / (m * L**2) ) # Коэф. связи

W_n_1 = w_0
W_n_2 = sqrt(w_0**2 + 2*x**2)


y_m_1 = []
y_m_2 = []
x_m = []

while t <= 200:
    f_1 = 0.5 * (A_1 * cos(W_n_1 * t + f_0_1) + A_2 * cos(W_n_2 * t + f_0_2))
    f_2 = 0.5 * (A_1 * cos(W_n_1 * t + f_0_1) - A_2 * cos(W_n_2 * t + f_0_2))
    x_m.append(t)
    y_m_1.append(f_1)
    y_m_2.append(f_2)
    #plt.subplot(k)
    t += 0.01

grid1 = plt.grid(True)
plt.plot(x_m, y_m_1, 'b', linewidth=2)
plt.plot(x_m, y_m_2, 'r', linewidth=2)
plt.legend([f'f_2 - правый', f'f_1 - левый'], loc=4)


plt.show()


