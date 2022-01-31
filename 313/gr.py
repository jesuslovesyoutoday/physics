import numpy as np
from numpy import polyval, polyfit
import matplotlib.pyplot as plt
import math

x = [12, 10, 8, 6, 4]
y = [6.93, 3.67, 1.96, 1.27, 9.13]

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y[i]**2
	sumX += x[i]**2
	sumy += y[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))


print(k)

plt.scatter(x, y)
b, c= polyfit(x, y, 1)
y_pred = polyval([b, c], Xx
print(b, c)
plt.plot(x, y_pred)
#plt.plot(x, y)
plt.title("Зависимость момента сил от количества шариков", fontsize = 20)
plt.xlabel("n", fontsize = 20)
plt.ylabel("M*10^-7", fontsize = 20)
plt.grid()
plt.show()
