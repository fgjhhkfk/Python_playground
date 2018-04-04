import urllib2
import os
from bs4 import BeautifulSoup


pfad = "/media/web/rezepte/"

for filename in os.listdir(pfad):

    url = pfad + filename
    print url
    # # url = "http://hjk.diskstation.me/rezepte/Lachscurry.html"

    # # aResp = urllib2.urlopen(url)
    # # r = aResp.read()

    soup = BeautifulSoup(open(url).read(), 'lxml')

    # Zubereitung finden
    # todo: den text der zuberteitung so beschneiden, dass nur noch die zubereitung
    #       drin steht
    res = soup.find('zubereitung')
    print res.text

    # zutataten finden
    # res = soup.find('zutaten')
    # print res.p.text
    raw_input("press somethin to continue ...")


