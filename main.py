from script.database import *
from script.json import *

from flask import Flask, render_template, request, url_for, flash, redirect, jsonify

MARKUP = """ 
    <tr>
        <td class="align-middle" id="titoloLibro" style="padding: 0.25rem"><--titolo--></td>
        <td class="align-middle" style="padding: 0.25rem">
            <div class="dropdown" style="float:right">
                <button class="btn" type="button" data-bs-toggle="dropdown" id="btnMenu">
                    <img src = "static/img/more-vertical.svg" alt="puntini"/>
                </button>
                <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">
                    <li class="info"><a class="dropdown-item" id="info" href="#1">Info</a></li>
                    <li class="modifica"><a class="dropdown-item" id="modifica" href="#2">Modifica</a></li>
                    <li class="elimina"><a class="dropdown-item" id="elimina" value="<--id-->" href="#3">Elimina</a></li>
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


@app.route('/create', methods=('GET', 'POST'))
def create():
    return redirect(url_for('index'))


@app.route('/cancella', methods=('POST', 'GET'))
def cancella():
    data = {}
    data['id'] = request.values.get('id')
    cancella_libro(data['id'])
    return jsonify(data)


@app.route('/provaTabella')
def provaTabella():
    return render_template('prova-tabella.html')


@app.route('/provaForm')
def provaForm():
    return render_template('prova-form.html')


@app.route('/provaAjax')
def provaAjax():
    return render_template('prova-ajax.html')


@app.route('/prova', methods=('POST', 'GET'))
def prova():
    data = {}
    data['id'] = request.values.get('id')
    return jsonify(data)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


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

    print('1 ' + str(titolo) + '    2 ' + str(autore) + '    3 ' + str(tipo) +
          '    4 ' + str(stato) + '    5 ' + str(pubblicazione) + '    6 ' +
          str(pagine) + '    7 ' + str(prezzo) + '    8 ' + str(inizio) +
          '    9 ' + str(fine) + '    10 ' + str(note))

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
        aggiungi(titolo=titolo, tipo=tipo, stato=stato)
    else:
        data['success'] = False
        data['errors'] = errors

    libro = get_libro(libro_titolo=titolo)
    print(libro['titolo'], libro['id'])
    data['markup'] = MARKUP.replace('<--titolo-->', libro['titolo'] + ' - ' +
                                    str(libro['id'])).replace(
                                        '<--id-->', str(libro['id']))
    temp = jsonify(data)
    return temp


app.run(host='0.0.0.0', port=81)
