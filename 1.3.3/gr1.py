import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
x = []
v = [0.5, 1, 1, 1, 1, 1, 1, 1, 1]
t = [7.38, 7.2, 6.49, 5.76, 4.85, 4.19, 4.02, 3.69, 3.56]
y = [11, 27, 39, 57, 72, 90, 108, 125, 143]

for i in range(len(v)):
    x.append(v[i]/t[i])

for i in range(len(y)):
    y[i] = y[i]*1.96
plt.scatter(x, y)
plt.plot(x, y)
plt.grid()

plt.xlabel('расход, м^3/с')
plt.ylabel('перепад давлений, Па')
plt.title('Для трубки l = 50 (см), R = 3.95 (мм)')

X = []
Y = []

for i in range(3):
    X.append(x[i])
    Y.append(y[i])

b, c = polyfit(X,Y,1)
y_pred = polyval([b, c], X)

MSE = np.sqrt(np.sum((Y-y_pred)**2)/6)
print(MSE)

print(b, c)
plt.plot(X, y_pred)

plt.show()
#plt.savefig('50 3,95')
