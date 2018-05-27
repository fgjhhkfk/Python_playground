# -*- coding: utf-8 -*-
import time
import numpy as np
from time import localtime, strftime

while True:
    f = open('/media/web/thermometer/temp.dat','a')
    Zeit = strftime("%d.%m.%Y_%H:%M:%S", localtime())
    rndmnbr = np.random.randint(-100,100)
    f.write(Zeit + ' ' + str(rndmnbr) + '\n')
    f.close()
    print Zeit
    time.sleep(5)

