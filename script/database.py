import sqlite3

LEGGI = """SELECT * FROM libri"""
CANCELLA = """DELETE FROM libri"""
CANCELLA_LIBRO = """DELETE FROM libri WHERE id=<--id-->"""
CERCA_ID = """SELECT * FROM libri WHERE id = <--id-->"""
CERCA_TITOLO = """SELECT * FROM libri WHERE titolo = "<--titolo-->" """
INSERISCI = """INSERT INTO libri (titolo,tipo,stato,autore,pubblicazione,pagine,prezzo,inizio,fine,note) VALUES (
  "<--titolo-->",
  "<--tipo-->",
  "<--stato-->",
  "<--autore-->",
  "<--pubblicazione-->",
  "<--pagine-->",
  "<--prezzo-->",
  "<--inizio-->",
  "<--fine-->",
  "<--note-->"
);"""
MODIFICA = """UPDATE libri SET 
  titolo="<--titolo-->",
  tipo="<--tipo-->",
  stato="<--stato-->",
  autore="<--autore-->",
  pubblicazione="<--pubblicazione-->",
  pagine="<--pagine-->",
  prezzo="<--prezzo-->",
  inizio="<--inizio-->",
  fine="<--fine-->",
  note="<--note-->"
  WHERE id=<--id-->; """


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


#CANCELLA UN LIBRO IN BASE ALL'ID
def cancella_libro(libro_id):
    connessione = connetti()
    connessione.execute(CANCELLA_LIBRO.replace("<--id-->", str(libro_id)))
    connessione.commit()
    connessione.close()


#OTTINEI I DATI DI UN LIBRO IN BASE ALL'ID
def get_libro(libro_id=None, libro_titolo=None):
    connessione = connetti()
    cur = connessione.cursor()
    if (libro_id != None):
        comando = CERCA_ID.replace("<--id-->", str(libro_id))
        print("id not null")
    elif (libro_titolo != None):
        comando = CERCA_TITOLO.replace("<--titolo-->", str(libro_titolo))
        print("titolo not null")
    else:
        print("errore")
        return
    post = cur.execute(comando).fetchone()
    connessione.commit()
    connessione.close()
    if post is None:
        print('no')
    return post


def modifica_libro(data):
    comando = MODIFICA.replace('<--titolo-->', data['titolo']).replace(
        '<--tipo-->',
        data['tipo']).replace('<--stato-->', data['stato']).replace(
            '<--autore-->', data['autore']).replace(
                '<--pubblicazione-->', data['pubblicazione']).replace(
                    '<--pagine-->', data['pagine']).replace(
                        '<--prezzo-->', data['prezzo']).replace(
                            '<--inizio-->', data['inizio']).replace(
                                '<--fine-->',
                                data['fine']).replace('<--note-->',
                                                      data['note']).replace(
                                                          '<--id-->',
                                                          data['id'])
    print(comando)
    connessione = connetti()
    cur = connessione.cursor()
    risultato = cur.execute(comando)
    connessione.commit()
    connessione.close()
    return risultato