import matplotlib.pyplot as plt
import scipy
import numpy as np
import math
fig, ax= plt.subplots()

from matplotlib.patches import Polygon


#a, b = 0, 0.004625000000000001
x = np.linspace(0, 10)

#ax.vlines(0, y.min(), y.max())
#ax.vlines(0.004625000000000001, y.min(), y.max())
#ix = np.linspace(a, b)
#iy = plt(ix)
#verts = [(a, 0), *zip(ix, iy), (b, 0)]
#poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
#ax.add_patch(poly)

#ax.text(0.5* (a + b), 18, r"Q = 2.912 (г/с)",
        #horizontalalignment='center', fontsize=10)

data = []
x = []
y = []

graph2 = plt.plot([0, 0],[0, 25])
        #graph3 = plt.plot([0.0063, 0.0063],[0, 10.031])
        #graph4 = plt.plot([0, 0.0063],[0, 0])
with open('30kalibr.txt', 'r') as reading:
    file_input = reading.read().split('\n')

for row in file_input:
    data.append(row.split(','))

for i in range(108):
    x.append((float(data[i][0])-68)*0.00025)
    y.append(math.sqrt(int(abs(float(data[i][1]))*2/1.2)))

for i in range(107):
    graph1 = plt.plot([x[i], x[i+1]], [y[i], y[i+1]])

ax.plot(x, y)
ax.grid()

ax.set_xlabel('расстояние, м')
ax.set_ylabel('скорость, м/с')

ax.set_title('График скорости струи на расстоянии 30 мм')
#plt.show()
plt.savefig("v30.png")

