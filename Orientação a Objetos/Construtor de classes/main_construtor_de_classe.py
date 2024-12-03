class Cliente:

    def __init__(self, nome, email): #Construtor de classe.
        self.nome = nome
        self.email = email
    
    def exibir(self):
        print(self.nome, self.email)


    def chamar_exibir (self):
        self.exibir()

pedro = Cliente("Pedro", "email@email.com")


print("-----------------")
pedro.exibir()
print("-----------------")
