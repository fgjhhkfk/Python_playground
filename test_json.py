import json
import numpy as np
import matplotlib.pyplot as plt

res = {}
res['xdata'] = range(0,21)
res['ydata'] = np.random.randint(0, 10, len(res['xdata'])).tolist()

print type(res['ydata'])
print type(res['xdata'])

with open('test.json', 'w') as f:
    json.dump(res, f, indent=2)


plt.figure
plt.plot(res['xdata'], res['ydata'])
plt.show()
