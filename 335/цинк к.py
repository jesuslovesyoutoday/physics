import math
x = [236.6, 386.2, 535.8, 685.4, 835, 984.6]
y = [240, 480, 680, 800, 920, 1040]
sumy = sumx = sumX = sumY = 0
for i in range(len(x)):
	sumY += y[i]**2
	sumX += x[i]**2
	sumy += y[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k = ", k)
