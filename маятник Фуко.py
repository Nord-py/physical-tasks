import matplotlib.pyplot as plt
from math import pi,e,sin,sqrt,cos

fig, l = plt.subplots()
grid1 = plt.grid(True)

g = 9.81 # УСП
l = 3 # Длинна нити
w = 0.2
f = 20
w_0 =sqrt(g/l)
w_z = w*sin(f)
W = sqrt(w_0**2+w_z**2)
w_p = W+w_z
w_m = W-w_z
x_c = []
y_c = []
t_c = []
z_c = []
t = 0.001
x_0 = 1
v_0 = 1

print(w_z/W)

C1 = 1
C2 = 1
while t<16:
    #z = e**(-1j*w*sin(f*t)) * (C1*cos(w_0**2 * t)+C2*sin(w_0**2 * t))              # (e**(-1j*W*sin(t*f))) * (C1*e**(1j*w*t)+C2*e**(-1j*w*t))  #(C1*e**(1j*sqrt(g/(l*t))) + C2*e**(-1j*sqrt(g/(l*t)))) * e**(-1j*W*t*sin(f))
    x =  v_0/W * sin(W*t)*sin(w_z*t)                                                   #x_0*w_m/(2*W) * cos(w_p*t) + x_0*w_p/(2*W) * cos(w_m*t)
    y =  v_0/W * sin(W*t)*cos(w_z*t)                                                   #-x_0*w_m/(2*W) * sin(w_p*t) + x_0*w_p/(2*W) * sin(w_m*t)
    x_c.append(x)
    y_c.append(y)
    #z_c.append(z)
    t_c.append(t)
    t+=0.0001

plt.plot(x_c,y_c,)
#plt.plot(z_c,t_c,)
#plt.plot(t_c,x_c,)
#plt.plot(t_c,y_c,)
#plt.plot(t_c,z_c,)
plt.show()
