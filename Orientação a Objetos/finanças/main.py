from utilitarios import (cadastrar_categoria, cadastrar_transacao, saldo_total)


# categorias
categorias_receitas = cadastrar_categoria("Receitas")
categorias_contas = cadastrar_categoria("Contas Fixas")
categorias_viagem = cadastrar_categoria("Viagem")
categorias_lazer = cadastrar_categoria("Lazer")

# transacao
cadastrar_transacao(descricao = "salario Jan/2024", valor= 1000.0, categoria=categorias_receitas)

cadastrar_transacao(descricao = "Tigrinho", valor= 50.0, categoria=categorias_receitas)

cadastrar_transacao(descricao = "Ingresso", valor= -150.0, categoria=categorias_lazer)

cadastrar_transacao(descricao = "Conta de Luz", valor= -100.0, categoria=categorias_contas)

cadastrar_transacao(descricao = "Viagem", valor= -400.0, categoria=categorias_viagem)

total = saldo_total()

print("saldo Total: ", total)