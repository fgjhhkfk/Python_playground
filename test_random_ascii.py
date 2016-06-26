import random
import string
import numpy as np


for j in range(10):
    a = [random.SystemRandom().randint(32,127) for i in range(1000)]
##    a = ''.join([chr(random.SystemRandom().randint(0,31)) for i in range(100)])
##    a = ''.join([chr(random.SystemRandom().randint(32,127)) for i in range(100)])
    print 'Minimum: ' + str(min(a)) + ' - Mittelwert: ' + str(np.mean(a)) + ' - Maximum: ' + str(max(a))
