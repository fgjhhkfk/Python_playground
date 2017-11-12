from matplotlib import style
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

style.use('fivethirtyeight')

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
y = np.array([1.2, 3, 6, 2, 4, 3.4, 8, 7.6, 9, 6.5])

# Geradengleichung: y = mx + b

m = (mean(x*y) - mean(x)*mean(y)) / (mean(x**2) - (mean(x))**2)
b = mean(y) - m*mean(x)
print m
print b

# Gerade fitten
geradenfit = [m*xn + b for xn in range(0, max(x), 1)]

print max(x)
plt.scatter(x, y)
plt.plot(xrange(0, max(x), 1), geradenfit, color='r')
plt.show()
