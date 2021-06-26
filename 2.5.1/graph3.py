import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit

x = [26, 30, 35, 40, 45, 50, 55, 60]
y = [179., 178, 177, 176, 175, 174, 173, 171]

for i in range(len(y)):
    y[i] = y[i] * 0.1 * 9.8 * 0.55 + x[i] * 0.121
    
x1 = [30, 35, 40, 45, 50, 55]
y1 = y[1:7]

plt.plot(x1, y1)
plt.scatter(x, y)
plt.grid()

plt.xlabel('Т, С', fontsize = 12)
plt.ylabel('U/F, мПа*м', fontsize = 12)
plt.title('Зависимость пов-ной эн-гии ед. площади от температуры', fontsize = 11)

#b, c = polyfit (x1, y1, 1)
#y_pred = polyval([b, c], x1)

#mse = np.sqrt(np.sum((y1-y_pred)**2)/6)
#print(mse)

#print(b, c)
#plt.plot(x1, y_pred)

#plt.show()
plt.savefig('3.png')
