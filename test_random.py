import numpy as np
import matplotlib.pyplot as plt

##plt.xkcd()

anzp = 100

ag = np.random.randint(1,256,size=anzp)
an = np.random.normal(128,50,anzp)

plt.subplot(221)
plt.plot(ag,'.r', label='asdf')
plt.legend(loc='upper right', bbox_to_anchor=(.5, .0, .5, .0))

plt.subplot(222)
plt.plot(an,'.r', label='asdf')
plt.legend()
plt.legend(loc='upper right', bbox_to_anchor=(.5, .5))

plt.subplot(223)
plt.hist(ag, label='asdf')
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

plt.subplot(224)
plt.hist(an)

plt.show()
