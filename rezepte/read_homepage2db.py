'''hjk.diskstation.me/rezepte.html lesen
jedem der vorhandenen Links folgen
links von allen unterseiten lesen
jeden link, jedes bild, jeden Titel in die DB schreiben
jedem link folgen, und zutaten und zubereitung auch in die db schreiben'''


from bs4 import BeautifulSoup

import rezepte as rz

rz.create_recipie_db('foobar.sqlite')

base_url = '/media/web/'
with open(base_url + 'rezepte.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    navigation = soup.find(class_='navigation')
    navlinks = navigation.find_all('a')

for navlink in navlinks:
    # print navlink.get('href')
    # print(base_url + navlink.get('href'))
    with open(base_url + navlink.get('href')) as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        # print(soup)

        content = soup.find(class_='content')
        rezepte = content.find_all('a')
        rezepte = rezepte[1::2]
        thumbnails = content.find_all('img')
        kategorie = navlink.get('title')
        tags = 'wasser'
        # for link in rezepte:
        for i in range(1, len(rezepte)):
            with open(base_url + rezepte[i].get('href')) as html_file:
                soup = BeautifulSoup(html_file, 'lxml')
                zubereitung_raw = soup.find('zubereitung')
                zubereitung = zubereitung_raw.find_all('p')[1:]
                bild = zubereitung_raw.find('img')
                zutaten = soup.find('zutaten')
                # print('\n')
                # print(rezepte[i].get('href').split('/')[-1].split('.')[0])
                # print(rezepte[i].get('href'))
                # print(bild.get('src'))
                # print(thumbnails[i].get('src'))
                # print(zutaten)
                # print(zubereitung[1::])
                # print(kategorie)
                # raw_input("press somethin to continue ...")
                rz.write2db(rezepte[i].get('href').split('/')[-1].split('.')[0],
                            rezepte[i].get('href'),
                            bild.get('src'),
                            thumbnails[i].get('src'),
                            zutaten,
                            zubereitung[1::],
                            kategorie,
                            tags)

'''
Zubereitung und Zutaten muessen noch aufgehuebscht werden
die Rezepte Kategorien zuordnen (main dolce ...), natuerlich in die DB
Tags mit in die DB aufnehmen
'''
