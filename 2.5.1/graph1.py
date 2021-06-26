import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
import math

x = [26, 30, 35, 40, 45, 50, 55, 60]
y = [179.33, 178, 176.66, 176, 175, 173.66, 173, 171]

for i in range(len(y)):
    y[i] = y[i] * 0.1 * 9.8 * 0.55
    
Y = 0
X = 0
YY = 0
XX = 0

for i in range(len(y)):
	YY += y[i]**2
	XX += x[i]**2
	Y += y[i]
	X += x[i]
	
X = X/8
Y = Y/8
XX = XX/8
YY = YY/8


plt.plot(x, y)
plt.scatter(x, y)
plt.grid()

plt.xlabel('Т, С', fontsize = 12)
plt.ylabel('σ, мПа*м', fontsize = 12)
plt.title('Зависимость коэффициента поверхностного натяжения от температуры', fontsize = 11)

b, c = polyfit (x, y, 1)
y_pred = polyval([b, c], x)

mse = np.sqrt(np.sum((y-y_pred)**2)/6)
print(mse)

print(b, c)
plt.plot(x, y_pred)

print(1/math.sqrt(8)*math.sqrt((YY - Y**2)/(XX - X**2) - b**2))

plt.show()
#plt.savefig('1.png')

