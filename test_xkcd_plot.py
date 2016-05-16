import matplotlib.pyplot as plt
import numpy as np

y = np.random.rand(10)
y2 = np.random.rand(10)
##plt.xkcd()    
plt.bar(range(len(y)), y, color='r')
plt.bar(range(len(y)), y2, color='b')
plt.show()


plt.style.use('grayscale')
y = np.random.rand(10)
y2 = np.random.rand(10)
##plt.xkcd()    
plt.bar(range(len(y)), y, color='r')
plt.bar(range(len(y)), y2, color='b')
plt.show()

