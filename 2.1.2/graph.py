import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
import math

x = [0.5, 1, 2, 5]
y = [1.45, 1.3, 1.28, 1.27]

    
Y = 0
X = 0
YY = 0
XX = 0

for i in range(len(y)):
	YY += y[i]**2
	XX += x[i]**2
	Y += y[i]
	X += x[i]
	
X = X/4
Y = Y/4
XX = XX/4
YY = YY/4

plt.scatter(x, y)
plt.plot(x, y)
plt.grid()

b, c, d = polyfit (x, y, 2)
y_pred = polyval([b, c, d], x)
print(b, c, d)
plt.plot(x, y_pred)
print(1/math.sqrt(4)*math.sqrt((YY - Y**2)/(XX - X**2) - b**2))

plt.xlabel('время открытия крана')
plt.ylabel('показатель адиабаты')
plt.title('зависимость показателя адиабаты воды от времени открытия крана')
#plt.legend()

plt.show()
