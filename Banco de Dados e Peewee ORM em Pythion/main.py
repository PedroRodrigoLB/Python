from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

# Crenado Usuarios para o B.D

    # usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="123456")

    # Usuario.create(nome="Pedro", email="pedro@teste.com", senha="123456")
    # Usuario.create(nome="Rodrigo", email="rodrigo@teste.com", senha="123456")
    # Usuario.create(nome="Luana", email="luana@teste.com", senha="123456"

#---------------------------------------------------------------------------------

# Confirmando os dados armazenados

    # lista_usuarios = Usuario.select()
    # print("Lista usuarios:")

    # for u in lista_usuarios:
    #     print("--", u.id, u.nome, u.email)

#---------------------------------------------------------------------------------

# Obtendo um usuario atraves do "id"

    # usuario1 = Usuario.get(Usuario.id == 1)

    # print("Usuario pelo id:", usuario1.id, usuario1.nome)

#---------------------------------------------------------------------------------

# Realizando a busta atraves de um email

    # rodrigo = Usuario.get(Usuario.email == "rodrigo@teste.com")

    # print("Usuario: ", rodrigo.id, rodrigo.nome, rodrigo.email)

#---------------------------------------------------------------------------------

# Realizando update no B.D

    # luana = Usuario.get(Usuario.email == "luana@teste.com")
    # luana.nome = "Luana Python"
    # luana.save()

    # print("Luana atualizada: ", luana.nome)

#---------------------------------------------------------------------------------

# Testando o atributo unico para email onde não pode ter repetição

    # print("Tentando criar um usuario com e-mail duplicado")

    # try:
    #     usuario_duplicado = Usuario.create(nome="Duplicado", email="teste@teste.com", senha="123456")

    # except:
    #     print("E-mail existente!")

#---------------------------------------------------------------------------------

# Deletando um dado no B.D

    # usuario_deletado = Usuario.get (Usuario.email == "teste@teste.com")
    # usuario_deletado.delete_instance ()

    # try:
    #     Usuario.get (Usuario.email == "teste@teste.com")
    # except:
    #     print ("Usuario deletado!")

#---------------------------------------------------------------------------------

# Criando um anúncio e praticar o uso da chave estrangeira

luana = Usuario.get (Usuario.email == "luana@teste.com")

anuncio = Anuncio.create(
    usuario = luana,
    titulo = "Video de Banco de Dados",
    descricao = "O projeto seria criar um video sobre banco de dados e ORM com Python",
    valor = 500.0
)

print ("Novo anuncio: ", anuncio.id, anuncio.titulo)