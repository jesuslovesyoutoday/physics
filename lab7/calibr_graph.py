import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()



x = [541, 1016.639]
y = [0, 57]
    

#ax.xaxis.set_major_locator(ticker.MultipleLocator(1016.639))

#ax.yaxis.set_major_locator(ticker.MultipleLocator(94))



ax.set_xlabel('давление, ед.')
ax.set_ylabel('давление, Па')
plt.grid()
ax.set_title('Калибровачный график')
ax.plot(x,y)
#ax.grid()
#plt.show()
plt.savefig("calibr.png")
