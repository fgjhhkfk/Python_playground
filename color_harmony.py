#!/bin/usr/pyhon
""" gibt ein Komplementaerfarbenpaar aus dem HSV Farbkreis wieder """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr
from matplotlib import cm
import math

x = np.linspace(1, 10, 100)
y = np.linspace(1, 2*np.pi, 100)
[X, Z] = np.meshgrid(x, y)


scale = 256.0/360.0

# Auswahl eines Zufaelligen Winkels auf dem Farbkreis
winkel = np.random.random_integers(0, 360, 1)

# Bestimmung des gegenueberliegenden Winkels
co_winkel = (winkel + 180) % 360

print winkel
print co_winkel

winkel_scal = int(winkel * scale)
co_winkel_scal = int(co_winkel * scale)

print cm.hsv(winkel_scal)
print cm.hsv(co_winkel_scal)

ax1 = plt.subplot(1, 2, 1)
ax1.patch.set_facecolor(cm.hsv(winkel_scal))
#plt.pcolor(x, y, Z)
#plt.autoscale(axis='both', tight='both')
ax2 = plt.subplot(1, 2, 2)
ax2.patch.set_facecolor(cm.hsv(co_winkel_scal))

plt.show()
