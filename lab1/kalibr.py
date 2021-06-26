import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.ticker as ticker

from matplotlib import pyplot as plt

fig, ax = plt. subplots()

x = np.array([2730, 2475, 2110, 1785, 1485], dtype=float)
y = np.array([160, 140, 120, 100, 80], dtype=float)

p = np.polyfit(x,y, 1)
ya = np.polyval(p, x)
plt.plot(x, y, label = 'исходный график')
plt.plot(x, ya, label = 'аппроксимированная прямая')

#ax.plot(x,y)
ax.grid()

plt.xlabel('отсчеты АЦП', fontsize = 15)
plt.ylabel('мм рт. ст.', fontsize = 15)

ax.legend(fontsize = 10)

plt.title('Калибровочный график', fontsize = 20)




for i in range(2):
        print('x = ', x[i], ' ','y = ', ya[i],' ')
        print(ya)

plt.savefig('kalibr.png')
