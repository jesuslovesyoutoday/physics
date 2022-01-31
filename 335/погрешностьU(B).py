import math

x = [236.6, 386.2, 535.8, 685.4, 835, 984.6]
y1 = [0, 20, 60, 100, 140, 160]
y2 = [40, 120, 200, 280, 320, 360]
y3 = [240, 400, 560, 720, 880, 1040]
y4 = [200, 440, 600, 760, 840, 920]

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y1[i]**2
	sumX += x[i]**2
	sumy += y1[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k1 = ", k)

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y2[i]**2
	sumX += x[i]**2
	sumy += y2[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k1 = ", k)

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y3[i]**2
	sumX += x[i]**2
	sumy += y3[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k1 = ", k)

sumy = sumx = sumX = sumY = 0

for i in range(len(x)):
	sumY += y4[i]**2
	sumX += x[i]**2
	sumy += y4[i]
	sumx += x[i]

k = math.sqrt(abs(1/10 * (sumY - sumy**2) / (sumX - sumx**2) - 0.12**2))
print("k1 = ", k)

