# O Object-Relational Mapping (ORM) utilizado foi o "peewee"

# Importando todas as informações do "peewee"

from peewee import *

# Foi utilizado o SQLite como B.D por ser mais simples

# Criando o B.D
db = SqliteDatabase('freelancers.db')


# Criando as Tabelas

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db

class Anuncio(Model):
    usuario= ForeignKeyField(Usuario, backref='usuarios')
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()

    class Meta:
        database = db