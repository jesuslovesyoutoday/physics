import numpy as np
from numpy import polyval, polyfit
import matplotlib.pyplot as plt

x = []
y = []


with open("2.txt") as f:
	data = f.read().split('\n')
for i in range(1, len(data)):
	data[i] = (data[i]).split(' ')
n = int(data[0])
data = data[1:]

for i in range(n):
	x.append(float(data[i][0]))
	y.append(float(data[i][1]))

    

plt.scatter(x, y)
#plt.plot(x, y)
plt.axhline(y = 1.675022709)

b, c= polyfit (x, y, 1)
y_pred = polyval([b, c], x)
print(b, c)
plt.plot(x, y_pred)

plt.xlabel("f", fontsize = 20)
plt.ylabel("Rl", fontsize = 20)
plt.title("Зависимость сопротивления катушки от частоты", fontsize = 20)
plt.grid()
plt.show()
	
	#plt.savefig(str(i) + ".png")
	

    
    
