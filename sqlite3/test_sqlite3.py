import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE rezepte (
            Name text,
            Bild blob,
            Zutaten text,
            Zubereitung text,
            Kategorie text,
            Tags text
            )""")

name = 'gemuesesuppe'
bild = ''
zutaten = 'gemuese'
zubereitung = 'kochen und zwar ganz lange, und heiss'
kategorie = 'suppe'
tags = 'vegetarisch'
c.execute("INSERT INTO rezepte VALUES (?, ?, ?, ?, ?, ?)", (name, bild, zutaten, zubereitung, kategorie, tags))
conn.commit()


c.execute("SELECT * FROM rezepte WHERE tags='vegetarisch'")
print(c.fetchall())

conn.close()
