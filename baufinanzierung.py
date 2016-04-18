import numpy as np
import matplotlib.pyplot as plt


def zinsberechnung(K, Z, Rate, sondertilgung, zinsanpassung):
    j = 0
    bez = 0
    res = np.array([K])
    while K > 0:
        # Wird der Zins nach einer gewissen Zeit angepasst?
        if j  > zinsanpassung[0][0]:
            Z = zinsanpassung[1][0]
            print "Der neue Zins betraegt im " + str(j) + ". Jahr " + str(zinsanpassung[1][0]) + "%"
        
        # Kreditschuld nach Beruecksichtigung der Zinsen
        K = K + K*Z

        # Den Sonderfall abfangen, falls die letzte Rate groesser ist als die Restschuld
        if K<Rate:
            Rate=K
            print "Die letzte Rate war nur noch " + str(Rate) + "EUR"

        # Was wurde bislang bezahlt?
        bez = Rate + bez

        # Wie gross ist die verbleibende Kreditschuld?
        K = K - Rate

        # Sondertilgung in den entsprechenden Jahren abziehen
        if j in sondertilgung[0]:
            K = K - sondertilgung[1][sondertilgung[0].index(j)]
            bez = bez + sondertilgung[1][sondertilgung[0].index(j)]

        # ab einem gegebenen Jahr immer die gleiche sondertilgung abziehen
        if sondertilgung[2] and j >= sondertilgung[2][0] and sondertilgung[3][0]<K:
            K = K - sondertilgung[3][0]
            bez = bez + sondertilgung[3][0]

        res = np.append(res, K)
        j += 1
    return res, bez


# Modell 1
# 4260EUR/Jahr fuer Tilgung und Zins (entspricht 355/Monat)
K1 = 100000
T1 = 0.0336
Z1 = 0.015
zinsanpassung = ([13],[0.0215])
sondertilgung = ([],[],[],[])
Rate1 = K1*T1 + K1*Z1

print "Rate fuer den 1. Kredit: " + str(Rate1) + "EUR. Das Entspricht " + str(Rate1/12) + "EUR monatlich"
[res1, bez1] = zinsberechnung(K1, Z1, Rate1, sondertilgung, zinsanpassung)
print "Fuer den 1. Kredit bezahlt: " + str(bez1) + "EUR"
plt.plot(res1, 'og', label='Modell 1: ' + str(K1/1000) + 'KEUR, T ' + str(T1*100) + '%, Z ' + str(Z1*100) + '%')


# Modell 2
# 4260EUR/Jahr fuer Tilgung und Zins (entspricht 355/Monat)
K2 = 100000
T2 = 0.035
Z2 = 0.02
zinsanpassung = ([999],[0])
sondertilgung = ([1,2,4,5],[3000, 3000, 3000, 3000],[8],[4500])
Rate2 = K2*T2 + K2*Z2

print "Rate fuer den 2. Kredit: " + str(Rate2) + "EUR. Das Entspricht " + str(Rate2/12) + "EUR monatlich"
[res2, bez2] = zinsberechnung(K2, Z2, Rate2, sondertilgung, zinsanpassung)
print "Fuer den 2. Kredit bezahlt: " + str(bez2) + "EUR"
plt.plot(res2, 'or', label='Modell 2: ' + str(K2/1000) + 'KEUR, T ' + str(T2*100) + '%, Z ' + str(Z2*100) + '%')

# Modell 3
# 4500EUR/Jahr fuer Tilgung und Zins (entspricht 375/Monat)
Kreditsumme = 100000
Zins = 0.035
Tilgung = 0.02
zinsanpassung = ([999],[0])
sondertilgung = ([],[],[],[])
Rate = Kreditsumme*Tilgung + Kreditsumme*Zins

print "Rate fuer den x. Kredit: " + str(Rate) + "EUR. Das Entspricht " + str(Rate/12) + "EUR monatlich"
[rrr, bbb] = zinsberechnung(Kreditsumme, Zins, Rate, sondertilgung, zinsanpassung)
print "Fuer den x. Kredit bezahlt: " + str(bbb) + "EUR"
plt.plot(rrr, 'ok', label='Modell 3: ' + str(Kreditsumme/1000) + 'KEUR, T ' + str(Tilgung*100) + '%, Z ' + str(Zins*100) + '%')



plt.ylim([0, 100000])
plt.grid()
plt.legend()

plt.show()
