import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style

plt.xkcd()

def zinsberechnung(K, Z, Rate, sondertilgung, zinsanpassung):
    j = 0
    bez = 0
    res = np.array([K])
    while K > 0:
        # Wird der Zins nach einer gewissen Zeit angepasst?
        if j  > zinsanpassung[0][0]:
            Z = zinsanpassung[1][0]
        
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
            print 'Sondertilgung (Jahr ' +str(sondertilgung[0][sondertilgung[0].index(j)])+ '): ' + str(sondertilgung[1][sondertilgung[0].index(j)]) + 'EUR'

        # ab einem gegebenen Jahr immer die gleiche sondertilgung abziehen
        if sondertilgung[2] and j >= sondertilgung[2][0] and sondertilgung[3][0]<K:
            K = K - sondertilgung[3][0]
            bez = bez + sondertilgung[3][0]
            print 'Sondertilgung (Jahr ' + str(sondertilgung[2][0]) + '): ' + str(sondertilgung[3][0]) + 'EUR'

        res = np.append(res, K)
        j += 1
    return res, bez


# Modell 1 (Bausparer; 13Jahre mit 1.5% Zins; anschliessend 2.15%; Rate fest bei 440EUR)
K1 = 97000
Z1 = 0.015
T1 = 440.00*12/K1-Z1

zinsanpassung = ([13],[0.0215])
sondertilgung = ([],[],[],[])
Rate1 = K1*T1 + K1*Z1

print "\nRate fuer den 1. Kredit: " + str(Rate1) + "EUR. Das Entspricht " + str(Rate1/12) + "EUR monatlich"
[res1, bez1] = zinsberechnung(K1, Z1, Rate1, sondertilgung, zinsanpassung)
print "Fuer den 1. Kredit bezahlt: " + str(bez1) + "EUR"
plt.plot(res1, '-og', label='Modell 1: ' + str(K1/1000) + 'KEUR, T ' + str(T1*100) + '%, Z ' + str(Z1*100) + '%')


# Modell 2 (Anuitaetendarlehnen mit 10 Jahren Zinsbindung; Rate 560EUR)
K2 = 100000
Z2 = 0.0206
T2 = 560.00*12/K2-Z2
zinsanpassung = ([999],[0])
sondertilgung = ([1,2,4,5],[5000, 5000, 5000, 5000],[8],[4500])
Rate2 = K2*T2 + K2*Z2

print "\nRate fuer den 2. Kredit: " + str(Rate2) + "EUR. Das Entspricht " + str(Rate2/12) + "EUR monatlich"
[res2, bez2] = zinsberechnung(K2, Z2, Rate2, sondertilgung, zinsanpassung)
print "Fuer den 2. Kredit bezahlt: " + str(bez2) + "EUR"
plt.plot(res2, '-or', label='Modell 2: ' + str(K2/1000) + 'KEUR, T ' + str(T2*100) + '%, Z ' + str(Z2*100) + '%')

# Modell 3
# 4500EUR/Jahr fuer Tilgung und Zins (entspricht 375/Monat)
Kreditsumme = 100000
Zins = 0.02
Tilgung = 500.00*12/Kreditsumme-Zins
zinsanpassung = ([999],[0])
sondertilgung = ([],[],[],[])
Rate = Kreditsumme*Tilgung + Kreditsumme*Zins

print "\nRate fuer den x. Kredit: " + str(Rate) + "EUR. Das Entspricht " + str(Rate/12) + "EUR monatlich"
[rrr, bbb] = zinsberechnung(Kreditsumme, Zins, Rate, sondertilgung, zinsanpassung)
print "Fuer den x. Kredit bezahlt: " + str(bbb) + "EUR"
plt.plot(rrr, '-ob', label='Modell 3: ' + str(Kreditsumme/1000) + 'KEUR, T ' + str(Tilgung*100) + '%, Z ' + str(Zins*100) + '%')


plt.ylim([0, 100000])
plt.grid()
plt.legend()
plt.title('Verlauf der Restschuld')
plt.ylabel('Restschuld [EUR]')
plt.xlabel('Zeit [Jahre]')
plt.axvline(10, linewidth=2, linestyle = '--', color = 'r')
plt.axvline(20, linewidth=2, linestyle = '--', color = 'r')
plt.show()

