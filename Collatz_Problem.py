import numpy as np
import matplotlib.pyplot as plt
import time

t = time.time()
for n in range(1, 10000000):
    i = 0
    a = n
    l = []
    n_start = n
    while n != 1:
        if n < n_start:
            break
        i += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        l.append(n)    

elapsed = time.time()-t
print elapsed

##    print "Haben fuer %d %d Durchgaenge gebraucht" % (a, i)
    
##print np.shape(l)
    # fuer die zahlen von 1 bis 1000
    # solange  die zahl nicht gleich 1 ist
    # teile die zahl durch 2 wenn sie gerade ist
    # multipliziere die zahl mit 3 und subtrahiere 1 wenn sie ungerade ist.
