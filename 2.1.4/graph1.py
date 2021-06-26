import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x = [48.2, 71.2, 74.7, 78.5, 83.3, 86.9, 88.3]
y = [18.13, 18.18, 18.23, 18.28, 18.33, 18.38, 18.48]

plt.plot(x, y)
plt.grid()
plt.ylabel('сопротивление, Ом')
plt.xlabel('время, с')
plt.title('Железо')


#plt.show()
plt.savefig('Железо')
