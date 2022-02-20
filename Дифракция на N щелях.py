import matplotlib.pyplot as plt
from math import sin,sqrt,pi

fig, l = plt.subplots()
grid1 = plt.grid(True)

a = 0.001
b = 0.001
l = 0.00064   # длинна волны в мм
d = 0.001 # d = a+b, a - ширина щели, b - расстояние между щелями в мм
N = 1 # количество щелей
I_0 = 1 # Начальная интенсивность
I_m = []
s_f_m_1 = []
s_f_m_2 = []
k = 0.000001

while k<5:
    s_f_1 = k*l / d
    I = I_0 * (sin(pi*b*s_f_1/l))**2 * (sin(N*pi*d*s_f_1/l))**2 / ((pi*b*s_f_1/l)**2 * (sin(pi*d*s_f_1/l))**2)
    s_f_m_1.append(s_f_1)
    s_f_m_2.append(-s_f_1)
    I_m.append(I)
    k+=0.0001


plt.plot(s_f_m_1,I_m)
plt.plot(s_f_m_2,I_m)
plt.plot(s_f_m_1,I_m)
plt.show()
