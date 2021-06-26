import matplotlib.pyplot as plt
import scipy
import numpy as np
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

x = []
y = []
data = []

with open('30kalibr.txt', 'r') as reading:
    file_input = reading.read().split('\n')

for row in file_input:
    data.append(row.split(','))

for i in range(100):
    x.append((float(data[i][0])-68)*0.00025)
    y.append(float(data[i][1]))

ax.plot(x, y)
    

ax.plot(x, y)

#ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))

#ax.yaxis.set_major_locator(ticker.MultipleLocator(40))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(4))

ax.set_xlabel('расстояние, м', fontsize = 10)
ax.set_ylabel('давление, Па.', fontsize = 10)

plt.grid()

ax.set_title('График давления на расстоянии 30 мм', fontsize = 15)
#plt.show()
plt.savefig("davlenie30")



