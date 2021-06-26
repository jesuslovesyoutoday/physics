import matplotlib.pyplot as plt
fig, ax = plt.subplots()
import numpy as np
from numpy import polyval, polyfit
import math

xw = [20.04, 21.06, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
xc = [34, 33, 32, 31, 30, 29, 28, 27, 26, 25]
yw = [1958, 1991, 1858, 2124, 2256, 2389, 2655, 2787, 2920,3053, 3451, 3584, 3849, 4115, 4513, 4646]
yc = [4513, 4380, 4115, 3982, 3849, 3584, 3318, 3053, 2787, 2522]

print ('xw ', len(xw))
print ('xc ', len(xc))
print ('yw ', len(yw))
print ('yc ', len(yc))
x = xw + xc
y = yw + yc

    
Y = 0
X = 0
YY = 0
XX = 0

for i in range(len(y)):
	YY += y[i]**2
	XX += x[i]**2
	Y += y[i]
	X += x[i]
	
X = X/26
Y = Y/26
XX = XX/26
YY = YY/26


#plt.plot(x, y)
plt.scatter(xw, yw, label = 'нагрев')
plt.scatter(xc, yc, label = 'охлаждение')
plt.grid()

plt.xlabel('Т, С', fontsize = 15)
plt.ylabel('P, Па', fontsize = 15)
plt.title('Зависимость давления от температуры', fontsize = 20)
plt.legend(fontsize = 15)

b, c = polyfit (x, y, 1)
y_pred = polyval([b, c], x)

#mse = np.sqrt(np.sum((y-y_pred)**2)/26)
#print(mse)

print(b, c)
plt.plot(x, y_pred)

print(1/math.sqrt(26)*math.sqrt((YY - Y**2)/(XX - X**2) - b**2))

# к = 202.61954231231957; -2488.216367453311
# погрешность к = 8.447896981052844

plt.show()
