# Realizando CRUD completo em um Banco de Dados (B.D)
                # C REATE
    # C R U D   # R EAD
                # U PDATE
                # D ELETE

from database import db, Usuario, Anuncio

# Para conectar ao banco de dados realiza a chamada da função ".connect"
db.connect()


# Criação das tabelas caso não existam no banco de dados
# ".create_tables" é uma função de criação, nesse caso recebe os parametros "Usuario" e "Anuncio"
db.create_tables([Usuario, Anuncio])
# Caso a tabela exista sera utilizado a existente



# Crenado Usuarios para o B.D


# Para adicionar dados a tabela se utiliza a função ".create" e add os parametros que seram anexados a tabela
usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="123456")

Usuario.create(nome="Pedro", email="pedro@teste.com", senha="123456")
Usuario.create(nome="Rodrigo", email="rodrigo@teste.com", senha="123456")
Usuario.create(nome="Luana", email="luana@teste.com", senha="123456")

#---------------------------------------------------------------------------------

# Confirmando os dados armazenados

# "lista_usuarios" sera a variavel que ira receber a "class Usuario" com a função ".select()"
lista_usuarios = Usuario.select()
print("Lista usuarios:")

# Loop que ira percorre a lista de usuarios
for u in lista_usuarios:
    print("--", u.id, u.nome, u.email)

#---------------------------------------------------------------------------------

# Obtendo um usuario atraves do "id"

usuario1 = Usuario.get(Usuario.id == 1)

print("Usuario pelo id:", usuario1.id, usuario1.nome)

#---------------------------------------------------------------------------------

# Realizando a busta atraves de um email

rodrigo = Usuario.get(Usuario.email == "rodrigo@teste.com")

print("Usuario: ", rodrigo.id, rodrigo.nome, rodrigo.email)

#---------------------------------------------------------------------------------

# Realizando update no B.D

luana = Usuario.get(Usuario.email == "luana@teste.com")
luana.nome = "Luana Python"
luana.save()

print("Luana atualizada: ", luana.nome)

#---------------------------------------------------------------------------------

# Testando o atributo unico para email onde não pode ter repetição

print("Tentando criar um usuario com e-mail duplicado")

try:
    usuario_duplicado = Usuario.create(nome="Duplicado", email="teste@teste.com", senha="123456")

except:
    print("E-mail existente!")

#---------------------------------------------------------------------------------

# Deletando um dado no B.D

usuario_deletado = Usuario.get (Usuario.email == "teste@teste.com")
usuario_deletado.delete_instance ()

try:
    Usuario.get (Usuario.email == "teste@teste.com")
except:
    print ("Usuario deletado!")

#---------------------------------------------------------------------------------

# Criando um anúncio e praticando o uso da chave estrangeira

luana = Usuario.get (Usuario.email == "luana@teste.com")

anuncio = Anuncio.create(
    usuario = luana,
    titulo = "Video de Banco de Dados",
    descricao = "O projeto seria criar um video sobre banco de dados e ORM com Python",
    valor = 500.0
)

print ("Novo anuncio: ", anuncio.id, anuncio.titulo)
    

# Mais anuncios para compor o B.D

Anuncio.create(usuario = luana, titulo = "Anuncio 1", descricao = "Os 7 habitos de pessoas altamente eficazes", valor = 5000)
Anuncio.create(usuario = luana, titulo = "Anuncio 2", descricao = "Boas praticas de programação", valor = 5000)
Anuncio.create(usuario = luana, titulo = "Anuncio 3", descricao = "O poder infinito da sua mente", valor = 10000)

print ("anuncios da luana:")

anuncios_luana = Anuncio.select().join(Usuario).where(Usuario.email == "luana@teste.com")
# Tradução: Busque na tabela "Anuncio" incluindo a tabela "Usuarios" onde o email usuario seja igual a "luana@teste.com" 

for a in anuncios_luana:
    print ("--", a.id, a.titulo, a.valor)

#---------------------------------------------------------------------------------

# Deletando todos os dados da tabela "Anuncio"

Anuncio.delete().execute()

print("Quantidade de anuncios: ", Anuncio.select().count())
