import sqlite3

LEGGI = """SELECT * FROM libri"""
CANCELLA = """DELETE FROM libri"""
CERCA_ID = """SELECT * FROM libri WHERE id = <--id-->"""
CERCA_TITOLO = """SELECT * FROM libri WHERE titolo = '<--titolo-->'"""
INSERISCI = """INSERT INTO libri (titolo,tipo,stato,autore,pubblicazione,pagine,prezzo,inizio,fine,note) VALUES (
  '<--titolo-->',
  '<--tipo-->',
  '<--stato-->',
  '<--autore-->',
  '<--pubblicazione-->',
  '<--pagine-->',
  '<--prezzo-->',
  '<--inizio-->',
  '<--fine-->',
  '<--note-->'
);"""


#CONNETTITI AL DATABASE
def connetti(database='data/libri.db', valore=None):
    connessione = sqlite3.connect(database)
    connessione.row_factory = sqlite3.Row
    return connessione


#LEGGI TUTTA LA TABELLA
def leggi_tutto(database='data/libri.db'):
    connessione = connetti()
    libri = connessione.execute('SELECT * FROM libri').fetchall()
    connessione.close()
    return libri


#AGGIUNGI ELEMENTI ALLA TABELLA
def aggiungi(titolo,
             tipo,
             stato,
             autore='',
             pubblicazione='',
             pagine='',
             prezzo='',
             inizio='',
             fine='',
             note=''):
    libro = INSERISCI.replace('<--titolo-->', titolo).replace(
        '<--tipo-->', tipo).replace('<--stato-->', stato).replace(
            '<--autore-->',
            autore).replace('<--pubblicazione-->', pubblicazione).replace(
                '<--pagine-->',
                pagine).replace('<--prezzo-->', prezzo).replace(
                    '<--inizio-->',
                    inizio).replace('<--fine-->',
                                    fine).replace('<--note-->', note)
    connessione = sqlite3.connect('data/libri.db')
    cursore = connessione.cursor()
    print(libro)
    cursore.execute(libro)
    connessione.commit()
    connessione.close()
    return libro


#CANCELLA TUTTO IL CONTENUTO DELLA TABELLA
def cancella_tutto():
    connessione = connetti()
    connessione.execute('DELETE FROM libri')
    connessione.commit()
    connessione.close()


#OTTINEI I DATI DI UN LIBRO IN BASE ALL'ID
def get_libro(libri_id=None, libri_titolo=None):
    print(libri_titolo)
    connessione = connetti()
    cur = connessione.cursor()
    comando = CERCA_TITOLO.replace("<--titolo-->", libri_titolo)
    post = cur.execute(comando).fetchone()
    print(post['id'])
    connessione.commit()
    connessione.close()
    if post is None:
        print('no')
    return post


def prova_add():
    connessione = sqlite3.connect('data/libri.db')
    cursore = connessione.cursor()
    cursore.execute(aggiungi('I racconti di Cthulhu', 'Libro', 'Finito'))
    connessione.commit()
    connessione.close()


def prova_cerca(titolo):
    connessione = connetti()
    cur = connessione.cursor()
    comando = CERCA_TITOLO.replace("<--titolo-->", titolo)
    post = cur.execute(comando).fetchone()
    print(post['id'])
    connessione.commit()
    connessione.close()


#prova_cerca('prova08')