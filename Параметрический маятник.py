import matplotlib.pyplot as plt
from math import sin,sqrt,cos,pi,e


fig, ax = plt.subplots()
grid1 = plt.grid(True)

gr = 45 # Стартовый градус
alfa_start = (gr*pi)/180 # Стартовый градус в радианах
l = 1 # Длинна нити
g = 9.80665 # УСП
k = 0.25 # коэф. упругости
t = 1 # Время
M_alfa = []
t_alfa = []
s = 0.1 # Растяжение нити

while t<20:
    u = sqrt(g/l - k**2)
    alfa = e**(-k*t) * (alfa_start*cos(u*t) + (k*alfa_start)/u * sin(u*t))
    M_alfa.append(alfa)
    t_alfa.append(t)
    t+=0.3
    l+=s
    s = -s



ax.set_xlabel('t (с)')
ax.set_ylabel('Угол (Рад)')
plt.plot(t_alfa,M_alfa, linewidth = 4)
plt.show()


