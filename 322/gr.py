import matplotlib.pyplot as plt
import numpy as np
from numpy import polyval, polyfit

x = []
y = []
X = []
Y = []

f = [32.55, 15.95]
U = [0.197, 0.107]

with open("001.txt") as f:
	data = f.read().split('\n')

for i in range(1, len(data)):
	data[i] = (data[i]).split(' ')

n = int(data[0])
data = data[1:]

for i in range(n):
	x.append(float(data[i][0]))
	y.append(float(data[i][1]))

with open("007.txt") as f:
	data = f.read().split('\n')

for i in range(1, len(data)):
	data[i] = (data[i]).split(' ')

n = int(data[0])
data = data[1:]

for i in range(n):
	X.append(float(data[i][0]))
	Y.append(float(data[i][1]))

b, c, d, e, f, j = polyfit (x, y, 5)
y_pred = polyval([b, c, d, e, f, j], x)
print(b, c, d, e, f, j)
plt.plot(x, y_pred)

plt.scatter(x, y)
#plt.plot(x, y)

b, c, d, e, f, j = polyfit (X, Y, 5)
y_pred = polyval([b, c, d, e, f, j], X)
print(b, c, d, e, f, j)
plt.plot(X, y_pred)

plt.scatter(X, Y)
#plt.plot(X, Y)

plt.xlabel("f/fo", fontsize = 20)
plt.ylabel("U(f)/Uo", fontsize = 20)
plt.title("AЧХ", fontsize = 20)

plt.grid()
plt.show()
