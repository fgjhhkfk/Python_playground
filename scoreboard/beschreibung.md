Anzeigetafel fuer einen Spielstand
Farbe der Tafel individuell einstellbar
Knopf zum hoch und herunterzaehlen
Knopf zum schreiben des Ergebnisses in eine Datenbank
    - Tore spieler 1
    - Tore Spieler 2
    - Datum + Uhrzeit
Spieler Hinzufuegen
Link zu einer Statistikseite

Datenbank:
Eine Tabelle mit den Ergebnissen (s.o.)
    CREATE TABLE scores(id integer primary key, player1 text, player2 text, goals1 integer, goals2 integer, date blob);
Eine Tabelle mit Spielern
    Username text, Spielfarbe text
    Bild?
    CREATE TABLE users(id integer primary key, username text, color text);
