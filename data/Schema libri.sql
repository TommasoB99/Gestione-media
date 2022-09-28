CREATE TABLE libri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    tipo TEXT NOT NULL,
  	stato TEXT NOT NULL,
    autore TEXT,
    pubblicazione TEXT,
    pagine INTEGER,
    prezzo REAL,
    inizio TEXT,
    fine TEXT,
    note TEXT
)