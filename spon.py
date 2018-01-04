#!/usr/bin/python
""" Einlesen der Kommentare des Spiegel-Online Artikels und speichern derer in einer Datei """

import urllib2
import os
from bs4 import BeautifulSoup

DATEI = os.path.expanduser('~/foobar.txt')
URL_BASE = 'http://www.spiegel.de/fragments/community/'

f = open(DATEI, 'w')

# Schleife ueber alle Seiten
for i in range(1, 247, 5):
    # Von welcher url sollen die Daten gelesen werden
    url =  URL_BASE + 'spon-673646-' + str(i) + '.html'

    # Daten von der url einlesen
    aResp = urllib2.urlopen(url);
    r = aResp.read();

    # das ganze mit BeautifulSoup anschauen
    soup = BeautifulSoup(r, 'lxml')

    # Die Sektionen der class js-article-post-full-text finden und in Datei schreiben
    for content in soup.find_all('div', attrs={'class':'js-article-post-full-text'}):
        f.write(str(content))

f.close()
