import re 


def x_palindromo(s):
    #Remover caracteres não alfanuméricos e converter para minuúsculas
    x_limpo = re.sub(r'[^a-zA-Z0-9]','',s).lower()

    #Verificar se a string limpa é igual à sua reversa
    return x_limpo == x_limpo[::-1]

#Testando a função
entrada = str(input("Escreva uma frase: "))
print(x_palindromo(entrada)) 