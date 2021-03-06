import sqlite3
from datetime import date, datetime

def create_recipie_db(filename):
    sqlite_file = filename
    tabellenname = 'Rezepte'
    spalte1 = 'id'
    spalte2 = 'titel'
    spalte3 = 'link'
    spalte4 = 'bild'
    spalte5 = 'thumbnail'
    spalte6 = 'zutaten'
    spalte7 = 'zubereitung'
    spalte8 = 'kategorie'
    spalte9 = 'tags'
    spalte1_typ = 'INTEGER PRIMARY KEY'
    spalte2_typ = 'STRING'
    spalte3_typ = 'STRING'
    spalte4_typ = 'STRING'
    spalte5_typ = 'STRING'
    spalte6_typ = 'STRING'
    spalte7_typ = 'STRING'
    spalte8_typ = 'STRING'
    spalte9_typ = 'STRING'


    # verbindung erstellen
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('CREATE TABLE {tn}({nf1} {ft1},\
                                 {nf2} {ft2},\
                                 {nf3} {ft3},\
                                 {nf4} {ft4},\
                                 {nf5} {ft5},\
                                 {nf6} {ft6},\
                                 {nf7} {ft7},\
                                 {nf8} {ft8},\
                                 {nf9} {ft9})'\
            .format(tn=tabellenname, nf1=spalte1, ft1=spalte1_typ,\
                                    nf2=spalte2, ft2=spalte2_typ,\
                                    nf3=spalte3, ft3=spalte3_typ,\
                                    nf4=spalte4, ft4=spalte4_typ,\
                                    nf5=spalte5, ft5=spalte5_typ,\
                                    nf6=spalte6, ft6=spalte6_typ,\
                                    nf7=spalte7, ft7=spalte7_typ,\
                                    nf8=spalte8, ft8=spalte8_typ,\
                                    nf9=spalte9, ft9=spalte9_typ))

    conn.commit()
    conn.close()


def write2db(titel, link, bild, thumbnail, zutaten, zubereitung, kategorie, tags):
    spalte2 = 'titel'
    spalte3 = 'link'
    spalte4 = 'bild'
    spalte5 = 'thumbnail'
    spalte6 = 'zutaten'
    spalte7 = 'zubereitung'
    spalte8 = 'kategorie'
    spalte9 = 'tags'

    db = sqlite3.connect('foobar.sqlite')
    c = db.cursor()
    c.execute('''INSERT INTO Rezepte({nf1}, {nf2}, {nf3}, {nf4}, {nf5}, {nf6}, {nf7}, {nf8})\
            VALUES("{v1}","{v2}","{v3}","{v4}","{v5}","{v6}","{v7}","{v8}")'''\
            .format(\
            nf1=spalte2, v1=titel,\
            nf2=spalte3, v2=link,\
            nf3=spalte4, v3=bild,\
            nf4=spalte5, v4=thumbnail,\
            nf5=spalte6, v5=zutaten,\
            nf6=spalte7, v6=zubereitung,\
            nf7=spalte8, v7=kategorie,\
            nf8=spalte9, v8=tags))

    db.commit()



# create_recipie_db()
# write2db('Fischsuppe', './asdfasdfl', './bilder/asdfsdf.png', 'Fisch Wasser Sonstiges', 'Alles Warmmachen usw.')
