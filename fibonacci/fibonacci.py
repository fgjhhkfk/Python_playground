# Alles rund um die Fibonacci Folge

import matplotlib.pyplot as plt

modulator = 111
a = [0, 1]
r = 1000
m = [a[0]%modulator, a[1]%modulator]


def cross_sum(a):
    cs = a[-2]+a[-1]
    return cs


def find_last_fibunacci_number(vec, modulator):
    while vec[-1] < modulator:
        vec.append(cross_sum(vec[-2::]))
    return vec[-2]

lfn = find_last_fibunacci_number(a[:], modulator)

for i in range(0, r, 1):
    a.append(cross_sum(a))
    m.append(a[-1]%modulator)
    if m[-1] == 1 and m[-2] == 0:
        break

print 'Die ersten 10 Zahlen der Fibonacci Folge sind: \n' + str(a[0:10])
print 'Die letzte Fibonacci Zahl kleiner als ' + str(modulator) + ' ist ' + str(lfn)
if len(m) > r:
    print 'Innerhalb der ' + str(r) + ' Zahlen langen Folge wiederholt sich der Remainder der Fibonacci Folge nicht.'
else:
    print 'Die Remainder der Fibonacci Folge wiederholen sich mit dem Modulator ' + str(modulator) + ' alle ' + str(len(m)-2) + ' Zeichen.'

plt.subplot(111)
plt.plot(m)
plt.show()
