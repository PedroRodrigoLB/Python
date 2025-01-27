from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é: {self.email}")


pedro = Cliente(nome="pedro", email="pedro@email.com", idade=30)

pedro.exibir()