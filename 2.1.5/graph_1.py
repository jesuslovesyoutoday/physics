import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
import math

y = [175, 200, 350, 375, 400, 460, 470, 550, 575, 635, 660, 750, 820]
x = [1.09, 1.074, 1.15, 1.18, 1.177, 1.21, 1.24, 1.27, 1.28, 1.34, 1.38, 1.42, 1.49]

for i in range(len(y)):
	y[i] = y[i] * 9.8/1000
	
for i in range(len(x)):
	x[i] = x[i] - 1/(x[i])**2

plt.plot(x, y)
plt.scatter(x, y)
plt.grid()

plt.ylabel('сила, Н', fontsize = 20)
plt.xlabel('λ - 1/(λ)^2, ед.', fontsize = 20)
plt.title('Зависимость(λ - 1/(λ)^2) от силы', fontsize = 20)
#plt.title('Зависимость относительного удлиннения от силы', fontsize = 20)

b, c = polyfit (x, y, 1)
y_pred = polyval([b, c], x)

#mse = np.sqrt(np.sum((y-y_pred)**2)/6)
#print(mse)

print(b, c)
plt.plot(x, y_pred)

#print(1/math.sqrt(8)*math.sqrt((y - Y**2)/(XX - X**2) - b**2))

plt.show()
#plt.savefig('1.png')
