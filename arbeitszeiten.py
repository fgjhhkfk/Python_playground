#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re
import datetime as dt
import sys, getopt

def main(argv):
    Inputfile = ''
    Datum = ''
    try:
        opts, args = getopt.getopt(argv,"hd:i:",["Datum=","Inputfile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -d <Datum> -i <Inputfile>')
            sys.exit()
        elif opt in ("-d", "--Datum"):
            Datum = arg
        elif opt in ("-i", "--Inputfile"):
            Inputfile = arg
    print('Datum: "', Datum)
    print('Inputfile: "', Inputfile)

    t_search = Datum

    # Datei einlesen, und Spalten benennen
    df = pd.read_csv(Inputfile, header=None, sep=';')
    cols = ['Aktion', 'Zeit']
    df.columns = cols

    # Leerzeiche aus Zeitspalte enfernen, und umwandeln in ein Zeitformat
    df['Zeit'] = df['Zeit'].str.strip()
    df['Zeit'] = pd.to_datetime(df['Zeit'], format='%d.%m.%Y %H:%M:%S.%f')

    # Kalenderwochen berechnen und als Spalte einfuegen
    df['week'] = df['Zeit'].dt.week.apply(str)

    # Index auf die Spalte Zeit setzen
    df = df.set_index('Zeit')


    # Unterscheidung ob nach einer Kalenderwoche oder einem Tag gefilter werden
    # soll
    if re.search('(\d*)([kK][wW])(\d*$)', t_search):
        # Suche nach einer KW

        # Die Kalenderwoche (Zahl) aus dem uebergebenen Sting extrahieren
        t_search = re.search('(\d*)([kK][wW])(\d*$)', t_search)

        # Filtern der Spalte mit den Wochen nach der angegebenen Kalenderwoche und
        # der Indexpalte nach dem Jahr
        filt_week = df['week'] == t_search.group(3)
        filt_year = df.index > '01.01.2020'
        df_search = df.loc[filt_year].loc[filt_week]

    elif re.search('\d+.\d+.\d+', t_search):
        # Suche nach einem bestimmten Tag

        # Wandeln des uebergebenen Strings, dass er das richtige Format hat
        oT = dt.datetime.strptime(t_search, '%d.%m.%Y')
        sT = dt.datetime.strftime(oT, '%m.%d.%Y')

        df_search = df[sT]

    # Berechnung der Zeitdifferenzen
    print(df_search.index.to_series().diff().dt.total_seconds().fillna(0)/3600)

    # Offen:
    # Zeit von aussen uebergeben
    # Die Zeitdifferenzen nur anzeigen, wenn sie sinvoll sind.


if __name__ == "__main__":
    main(sys.argv[1:])
