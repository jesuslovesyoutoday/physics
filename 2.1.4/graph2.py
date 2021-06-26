import matplotlib.pyplot as plt
import numpy as NP
import scipy
from numpy import polyval, polyfit

fig, ax = plt.subplots()

y = [60.8, 67.5, 73.5, 78.3, 80.8, 82, 84.1]
x = [18.21, 18.26, 18.31, 18.36, 18.41, 18.46, 18.51]

Y = []
X = [18.21, 18.26, 18.31, 18.36, 18.41, 18.46]

for i in range (6):
    Y.append((x[i+1]-x[i])/(y[i+1]-y[i]))
    
    
a, b, c = polyfit(X, Y, 2)
y_pred = polyval([a, b, c], X)

print(a, b, c)

#plt.plot(X, Y)
print(Y)
plt.grid()

#x_out = NP.linspace(0, 2, 20)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid()

ax1.plot(X, y_pred,)
plt.xlabel('сопротивление, Ом')
plt.ylabel('dR/dT, Ом/с')
plt.title('Алюминий')


#plt.show()
plt.savefig('алюминий1')
