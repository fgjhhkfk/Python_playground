for n in range(1, 10000):
    i = 0
    a = n
    l = []
    while n != 1:
        i += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    print "Haben fuer %d %d Durchgaenge gebraucht" % (a, i)
    l.append(i)
print max(l)
    # fuer die zahlen von 1 bis 1000
    # solange  die zahl nicht gleich 1 ist
    # teile die zahl durch 2 wenn sie gerade ist
    # multipliziere die zahl mit 3 und subtrahiere 1 wenn sie ungerade ist.
