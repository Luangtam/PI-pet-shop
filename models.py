from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Telefone(db.Model):
    __tablename__ = "telefone"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    formacao = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Telefone {self.nome}>"
