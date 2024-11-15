
try:

    lista_itens = []

#Adicionar item
    def adicionar_item():
        print("====================")

        item = input("Digite o nome do item que deseja adicionar: ")
        nome = item.lower()
        repetido = False
        for n in lista_itens:

            if n == nome:

                repetido = True
                print("===============================") 
                print("Item já consta na lista")

        if nome and not repetido:
            lista_itens.append(nome)
            print("===============================") 
            print("item adicionado a lista")

# Remover item
    def remover_item():
        print("====================")

        item = input("Digite o nome do item para remover: ")
        nome = item.lower()
        nao_consta = True

        for n in lista_itens:

            if n==nome:

                nao_consta = False
                lista_itens.remove(nome)
                print("===============================") 
                print("item removido!!")
            

        if nome and nao_consta:
            print("====================")
            print("Item não consta na lsita")

# Informar lista
    def informa_lista():
        b = 0
        print("====================")
        for x in lista_itens:
            b += 1
            print(f"{b}. item: ",x)
        if not lista_itens:
            print("Lista vazia")
        print("=====================")

    while True:
    # Menu de escolha da função
        print("========== Lista de compra ============")
        print("1- Adicionar item a lista")
        print("2- Remover item da lista")
        print("3- Informação da lista")
        print("4- Encerrar programa")
        print("=======================================================")

        opcao = int( float( input("Digite a função desejavel: ")))
    
        # Chama função de adicionar
        if opcao == 1:   
            adicionar_item()
    
        # Cahama função de remover
        elif opcao == 2:
            remover_item()

        # Chama função de exibir a lista
        elif opcao == 3:
            informa_lista()

        # Encerra programa
        elif opcao == 4:
            print("=====================")
            print("Encerrando o programa!!!")
            print("=====================")
            break
    
        # Numeros invalidos
        elif opcao >=5 or opcao <=0:
            print("Opção invalida")

except:
    print("Erro inesperado!!")
