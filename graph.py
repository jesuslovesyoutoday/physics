import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

from matplotlib import pyplot as plt
fig, ax = plt.subplots()
data = []
x = []
y = []

with open("1kalibr.txt", 'r') as reading:
        file_input = reading.read().split('\n')

for row in file_input:
    data.append(row.split(' '))

for i in range(8155, 8410):
    y.append(float(data[i][0]))
    x.append(float(data[i][1])-4327.6)
p = np.polyfit(x,y, 1)
ya = np.polyval(p, x)

for i in range(2):
    print (x[i],' ', y[i],'\n' )


#plt.figure(figsize = (15, 10))

"""data1 = []
x1 = []
y1 = []

with open("2kalibr.txt", 'r') as reading:
    file_input = reading.read().split('\n')

for row in file_input:
    data1.append(row.split(' '))

for i in range(2005, 18139):
    y1.append(float(data1[i][0]))
    x1.append(float(data1[i][1])-6632)"""

plt.plot(x, y-ya, label = 'импульс')
#plt.plot(x1, y1, label = 'До нагрузки')

#plt.plot(x, ya, label = 'линейная составляющая')

plt.grid()
plt.xlabel('время,мс', fontsize = 15)
plt.ylabel('мм рт. ст.', fontsize = 15)

#plt.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
#plt.title('График зависимости артериального давления от времени', fontsize = 20)

ax.legend(fontsize = 10)

plt.show()
#plt.savefig('gr.png')
