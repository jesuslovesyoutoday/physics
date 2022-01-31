import matplotlib.pyplot as plt
import numpy as np
from numpy import polyval, polyfit
import math

x = [0, 0.16, 0.33, 0.51, 0.7, 0.85, 1.02, 1.19, 1.37]
y = [19, 166.1, 334.7, 519.1, 689.4, 793.2, 884.5, 954.8, 1007.1]

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y[i]**2*10**(-3)
	sumX += x[i]**2
	sumy += y[i]*10**(-3)
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))


print(k)

plt.scatter(x, y)
plt.title("Зависимость индукции мп от тока через магнит", fontsize = 20)
plt.xlabel("I, А", fontsize = 20)
plt.ylabel("B, мТл", fontsize = 20)
b, c = polyfit (x, y, 1)
Y = polyval([b, c], x)
yy = []
for i in range(len(y)):
    yy.append(y[i]*(10**(-3)))
B, C = polyfit(x, yy, 1)
YY = polyval([B, C], x)
print(B, C)
plt.plot(x, Y)
plt.show()
