import math
x = [0.2, 0.4, 0.6, 0.9]
y = [0.23, 0.44, 0.95, 1.06]
sumy = sumx = sumX = sumY = 0
for i in range(len(x)):
	sumY += y[i]**2
	sumX += x[i]**2
	sumy += y[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k1 = ", k)
