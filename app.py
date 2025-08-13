from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco
def get_db_connection():
    conn = sqlite3.connect('petshop.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criar tabelas se não existirem
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animal (
            id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT,
            raca TEXT,
            id_cliente INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamento (
            id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
            id_animal INTEGER,
            servico TEXT,
            data TEXT,
            FOREIGN KEY (id_animal) REFERENCES animal (id_animal)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

# Clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        conn.execute('INSERT INTO cliente (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)',
                     (nome, email, telefone, endereco))
        conn.commit()
        return redirect(url_for('clientes'))

    clientes = conn.execute('SELECT * FROM cliente').fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

# Animais
@app.route('/animais', methods=['GET', 'POST'])
def animais():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        raca = request.form['raca']
        id_cliente = request.form['id_cliente']
        conn.execute('INSERT INTO animal (nome, tipo, raca, id_cliente) VALUES (?, ?, ?, ?)',
                     (nome, tipo, raca, id_cliente))
        conn.commit()
        return redirect(url_for('animais'))

    animais = conn.execute('SELECT * FROM animal').fetchall()
    clientes = conn.execute('SELECT * FROM cliente').fetchall()
    conn.close()
    return render_template('animais.html', animais=animais, clientes=clientes)

# Agendamentos
@app.route('/agendamentos', methods=['GET', 'POST'])
def agendamentos():
    conn = get_db_connection()
    if request.method == 'POST':
        id_animal = request.form['id_animal']
        servico = request.form['servico']
        data = request.form['data']
        conn.execute('INSERT INTO agendamento (id_animal, servico, data) VALUES (?, ?, ?)',
                     (id_animal, servico, data))
        conn.commit()
        return redirect(url_for('agendamentos'))

    agendamentos = conn.execute('SELECT * FROM agendamento').fetchall()
    animais = conn.execute('SELECT * FROM animal').fetchall()
    conn.close()
    return render_template('agendamentos.html', agendamentos=agendamentos, animais=animais)

if __name__ == '__main__':
    app.run(debug=True)
