import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit

x = [26, 30, 35, 40, 45, 50, 55, 60]
y = []

for i in range(len(x)):
    y.append(x[i] * 0.121)

plt.plot(x, y)
plt.scatter(x, y)
plt.grid()

plt.xlabel('Т, С', fontsize = 12)
plt.ylabel('q, мПа*м', fontsize = 12)
plt.title('Зависимость теплоты образования ед. пов-ти жидкости от температуры', fontsize = 11)

#b, c = polyfit (x, y, 1)
#y_pred = polyval([b, c], x)

#mse = np.sqrt(np.sum((y-y_pred)**2)/6)
#print(mse)

#print(b, c)
#plt.plot(x, y_pred)

#plt.show()
plt.savefig('2.png')
