from flask import Flask
from configuration import configure_all


# inicializacao do Flask
app = Flask(__name__)

configure_all(app)


# execução
app.run(debug=True)  # "debug=True" ativa o modo desenvolvedor