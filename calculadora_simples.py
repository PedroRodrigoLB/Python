# Desafio calculadora Simples

def d():
    print("---------------------")
    print("O peração invalida")
    print("---------------------")

while True:

# Opeções de operações
    print("---------------------")
    print("Operações disponiveis")
    print("---------------------")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("---------------------")
    print("0: Sair")
    print("---------------------")
    operacao = int ( input ("Operação desejavel: "))
    print("---------------------")

    if operacao == 1:
        # Variavesi que serão informadas
        x = float(input("Valor 01: "))
        print("----------------")
        y = float(input("Valor 02: "))
    
        # Operação com as variaveis
        adicao = x + y

        # Retorna resultado da operação
        print("----------------")
        print("Resultado da adição: ", adicao)
        print("----------------")

    elif operacao == 2:
        # Variavesi que serão informadas
        x = float(input("Valor 01: "))
        print("----------------")
        y = float(input("Valor 02: "))
    
        # Operação com as variaveis
        subtracao = x - y

        # Retorna resultado da operação
        print("----------------")
        print("Resultado da subtração: ", subtracao)
        print("----------------")

    elif operacao == 3:
        # Variavesi que serão informadas
        x = float(input("Valor 01: "))
        print("----------------")
        y = float(input("Valor 02: "))
    
        # Operação com as variaveis
        multiplicacao = x * y

        # Retorna resultado da operação
        print("----------------")
        print("Resultado da multiplicação: ", multiplicacao)
        print("----------------")

    elif operacao == 4:
        # Variavesi que serão informadas
        x = float(input("Valor 01: "))
        print("----------------")
    
        # Evitando a divisão por zero
        def c():
            print("---------------------------------------------")
            print("Atenção o valor 02 deve ser diferente de zero")
            print("---------------------------------------------")

        
        while True:
            y = float(input("Valor 02: "))

            if y == 0:
                c()
            else:
                break

        # Operação com as variaveis
        divisao = x / y

        # Retorna resultado da operação
        print("----------------")
        print("Resultado da divisão: ", divisao)
        print("----------------")

    elif operacao >= 5:
        d()
    else:
        break
    


