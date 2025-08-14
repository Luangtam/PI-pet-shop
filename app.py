from flask import Flask, render_template
from models import db, Telefone

app = Flask(__name__)

# Configuração MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/nome_do_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/listar')
def listar():
    telefones = Telefone.query.all()
    return render_template("listar.html", telefones=telefones)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
