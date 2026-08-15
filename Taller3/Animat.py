import numpy as np
import matplotlib.pyplot as plt


for x in range(0, 300):
    fs= 200 + x 
    T=np.arange(0,0.1,1/fs) #eje x

    A=0.5
    f0=50

    Y=A*np.sin(2*np.pi*f0*T) #eje y
    plt.plot(Y, "*")
    plt.pause(0.000002)
plt.show()

