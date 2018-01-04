# Auslesen von Metadaten einer epub-Datei
# Umformattieren der Metatdaten --> ongoing
# Schreiben der Metadaten in eine Datenbank --> todo
# Metadatenuebersicht: https://de.wikipedia.org/wiki/EPUB

from ebooklib import epub
import os


def print_ebook_metadata(path2file):
    print('\n')
    print('PFAD:   ' + path2file)
    buch = epub.read_epub(path2file)

    # get_metadata gibt eine LISTE mit TUPEL zurueck, in denen STRINGS stecken
    # print path2file + ' hat kein Titelfeld.'

    titel = buch.get_metadata('DC', 'title')[0][0]
    print('TITEL:   ' + titel)

    # pruefen ob das Feld 'creator' vorhanden ist
    try:
        autor = buch.get_metadata('DC', 'creator')[0][0].split(' ')
        print(len(autor))
        print('AUTOR:   ' + autor[-1] + ',' + autor[-2])
        print('AUTOR:   ' + ' '.join(autor))

        # wenn der Dateiname den Autorennamen enthaelt, nichts machen
        if not path2file.__contains__(autor[-1]):
            if len(autor) > 1:
                print(path2file + ' --> ' + autor[-1] + ', ' + ' '.join(autor[:-1]) + ' - ' + titel)
            else:
                print(path2file + ' --> ' + autor[-1] + ' - ' + titel)

    except KeyError:
        print(path2file + ' --> ' + titel)


path = '/media/nas/ebooks/K/'

# ueber alle Dateien mit der Endung .epub iterieren
for i in os.listdir(path):
    if i.endswith('.epub'):
        print_ebook_metadata(path + i)
