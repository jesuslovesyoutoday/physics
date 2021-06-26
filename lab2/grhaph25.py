import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

from matplotlib import pyplot as plt
fig, ax = plt.subplots()
data = []
x = []
y = []

with open("55cal.txt", 'r') as reading:
    file_input = reading.read().split('\n')

for row in file_input:
    data.append(row.split(' '))

for i in range(len(data)-1):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))

plt.figure(figsize = (15, 10))
plt.plot(x, y)
plt.grid()
plt.xlabel('время, с', fontsize = 15)
plt.ylabel('уровень воды, мм', fontsize = 15)

plt.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
plt.title('График зависимости уровня воды от времени для 55 мм', fontsize = 20)

#plt.savefig('55.png')
plt.show()

