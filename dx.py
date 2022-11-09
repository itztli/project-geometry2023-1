#!/usr/bin/env python3

# Author: Victor De la Luz
# email: vdelaluz@enesmorelia.unam.mx
# License: GNU/GPL

import numpy as np
import matplotlib.pyplot as plt


# m(x-x0) = y-y0
# y = m(x-x0)+y0
def g(x,x0,y0,m):
    return m*(x-x0)+y0



x0 = np.pi/5.0
y0 = np.sin(x0)
m = np.cos(x0)

x = np.arange(-2*np.pi, 2*np.pi+0.1, 0.1)
y = np.sin(x)
line = g(x,x0,y0,m)


#print(x)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x,y)
ax.scatter(x0,y0,color='r')
ax.plot(x,line)

plt.show()
