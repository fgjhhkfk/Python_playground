"""
1. wenn gefordert ein neues sqlite file erstellen
2. 1. Spalte Datum + Zeitstempel einfuegen
3. 2.-n. Spalte einen Zufallswert eintragen
"""

import sqlite3
import random
from datetime import date, datetime

def create_db():
    sqlite_file = 'test.sqlite'
    tabellenname = 'Thermometer'
    spalte1 = 'zeitstempel'
    spalte2 = 'sensor1'
    spalte3 = 'sensor2'
    spalte4 = 'sensor3'
    spalte5 = 'sensor4'
    spalte1_typ = 'DATE'
    spalte2_typ = 'DECIMAL(3,2)'
    spalte3_typ = 'DECIMAL(3,2)'
    spalte4_typ = 'DECIMAL(3,2)'
    spalte5_typ = 'DECIMAL(3,2)'


    # verbindung erstellen
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('CREATE TABLE {tn}({nf1} {ft1}, {nf2} {ft2}, {nf3} {ft3}, {nf4} {ft4}, {nf5} {ft5})'\
            .format(tn=tabellenname, nf1=spalte1, ft1=spalte1_typ,\
                                    nf2=spalte2, ft2=spalte2_typ,\
                                    nf3=spalte3, ft3=spalte3_typ,\
                                    nf4=spalte4, ft4=spalte4_typ,\
                                    nf5=spalte5, ft5=spalte5_typ))

    conn.commit()
    conn.close()

def write2db(sensorvalue1, sensorvalue2, sensorvalue3, sensorvalue4):
    spalte1 = 'zeitstempel'
    spalte2 = 'sensor1'
    spalte3 = 'sensor2'
    spalte4 = 'sensor3'
    spalte5 = 'sensor4'
    zeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # zeit = datetime.utcnow()
    print(zeit)
    db = sqlite3.connect('test.sqlite')
    c = db.cursor()
    c.execute('''INSERT INTO Thermometer({nf1}, {nf2}, {nf3}, {nf4}, {nf5})\
            VALUES("{v1}", {v2}, {v3}, {v4}, {v5})'''\
            .format(nf1=spalte1, v1=zeit,\
            nf2=spalte2, v2=sensorvalue1,\
            nf3=spalte3, v3=sensorvalue2,\
            nf4=spalte4, v4=sensorvalue3,\
            nf5=spalte5, v5=sensorvalue4))

    db.commit()

def read_db2dict():
    cur = sqlite3.connect('test.sqlite').cursor()
    query = cur.execute('SELECT * FROM Thermometer')
    colname = [ d[0] for d in query.description ]
    result_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
    cur.close()
    cur.connection.close()
    return result_list

read_db2dict()
# create_db()
# write2db(random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
