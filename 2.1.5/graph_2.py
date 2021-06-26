import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
import math

y = [0.022, 0.029, 0.042, 0.067, 0.092, 0.115, 0.122, 0.123]
x1 = [7, 9, 18, 22, 26, 25, 28, 41]
x2 = [175, 200, 375, 400, 470, 460, 550, 635]
x = []
	
for i in range(len(x1)):
	x.append(x2[i]*9.8*x1[i]/1000)

plt.plot(x, y)
plt.scatter(x, y)
plt.grid()

plt.ylabel('ΔТ, °', fontsize = 20)
plt.xlabel('А, Дж', fontsize = 20)
#plt.title('Зависимость(λ - 1/(λ)^2) от силы', fontsize = 11)
plt.title('Зависимость приращения температуры от работы по адиабатическому расширению', fontsize = 20)

b, c = polyfit (x, y, 1)
y_pred = polyval([b, c], x)

#mse = np.sqrt(np.sum((y-y_pred)**2)/6)
#print(mse)

print(b, c)
plt.plot(x, y_pred)

Y = 0
X = 0
for i in range(len(x)):
	X+=x[i]**2
	Y+=y[i]**2

print(1/math.sqrt(13)*math.sqrt((Y)/(X) - b**2))

plt.show()
#plt.savefig('1.png')
