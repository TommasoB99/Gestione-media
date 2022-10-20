from script.database import *
from script.json import *

from flask import Flask, render_template, request, url_for, flash, redirect, jsonify

MARKUP = """ 
    <tr id="codice<--id-->" value="<--id-->">
        <td class="align-middle" id="titoloLibro" style="padding: 0.25rem"><--titolo--></td>
        <td class="align-middle" style="padding: 0.25rem">
            <div class="dropdown" style="float:right">
                <button class="btn" type="button" data-bs-toggle="dropdown" id="btnMenu">
                    <img src = "static/img/more-vertical.svg" alt="puntini"/>
                </button>
                <ul class="dropdown-menu" role="menu" aria-labelledby="menu1" data-id="<--id-->">
                    <li class="info"><a class="dropdown-item" id="info" href="#1">Info</a></li>
                    <li class="modifica"><a class="dropdown-item" id="modifica" href="#2">Modifica</a></li>
                    <li class="elimina"><a class="dropdown-item" id="elimina" href="#3">Elimina</a></li>
                </ul>
            </div>
        </td>
    </tr>"""

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    libri = leggi_tutto()
    #return render_template('index.html', libri=libri)
    return render_template('index.html', libri=libri)


@app.route('/info', methods=('POST', 'GET'))
def info():
    data = {}
    id = request.values.get('id')
    libro = get_libro(libro_id=id)
    parole = libro.keys()
    for i in range(11):
        data[parole[i]] = libro[i]
    return jsonify(data)


@app.route('/modifica', methods=('POST', 'GET'))
def modifica():
    data = {}
    errori = {}

    data['id'] = request.values.get('id')
    data['titolo'] = request.values.get('titolo')
    data['autore'] = request.values.get('autore')
    data['tipo'] = request.values.get('tipo')
    data['stato'] = request.values.get('stato')
    data['pubblicazione'] = request.values.get('pubblicazione')
    data['pagine'] = request.values.get('pagine')
    data['prezzo'] = request.values.get('prezzo')
    data['inizio'] = request.values.get('inizio')
    data['fine'] = request.values.get('fine')
    data['note'] = request.values.get('note')

    if (not data['titolo']):
        errori['titolo'] = 'inserisci un titolo'
    if (not data['stato']):
        errori['stato'] = 'inserisci uno stato'
    if (not data['tipo']):
        errori['tipo'] = 'inserisci un tipo'

    data['errori'] = errori
    print(modifica_libro(data))
    return jsonify(data)


@app.route('/cancella', methods=('POST', 'GET'))
def cancella():
    data = {}
    data['id'] = request.values.get('id')
    cancella_libro(data['id'])
    data['codice'] = '#codice' + str(data['id'])
    return jsonify(data)


@app.route('/form', methods=('GET', 'POST'))
def form():
    titolo = request.form.get("titolo")
    autore = request.form.get("autore")
    tipo = request.form.get("tipo")
    stato = request.form.get("stato")
    pubblicazione = request.form.get("pubblicazione")
    pagine = request.form.get("pagine")
    prezzo = request.form.get("prezzo")
    inizio = request.form.get("inizio")
    fine = request.form.get("fine")
    note = request.form.get("note")

    data = {}
    errors = {}

    if (not titolo):
        errors['titolo'] = 'inserisci un titolo'
    if (not stato):
        errors['stato'] = 'inserisci uno stato'
    if (not tipo):
        errors['tipo'] = 'inserisci un tipo'

    if (not errors):
        data['message'] = 'Libro Aggiunto Correttamente'
        data['success'] = True
        print('libro aggiunto')
        aggiungi(titolo=titolo,
                 tipo=tipo,
                 stato=stato,
                 autore=autore,
                 pubblicazione=pubblicazione,
                 pagine=pagine,
                 prezzo=prezzo,
                 inizio=inizio,
                 fine=fine,
                 note=note)
    else:
        data['success'] = False
        data['errors'] = errors

    libro = get_libro(libro_titolo=titolo)
    data['markup'] = MARKUP.replace('<--titolo-->', libro['titolo'] + ' - ' +
                                    str(libro['id'])).replace(
                                        '<--id-->', str(libro['id']))
    temp = jsonify(data)
    return temp


@app.route('/esporta')
def esporta():
    libri = leggi_tutto()
    database = []
    for x in libri:
        libro = {}
        parole = x.keys()
        for i in range(11):
            #print(str(parole[i])+": "+str(x[i]))
            libro[parole[i]] = x[i]
        database.append(libro)
    esporta_database(database)
    return ('', 204)


app.run(host='0.0.0.0', port=81)
