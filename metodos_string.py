# Construir codigo Palíndromo

# A função deve receber uma string como entrada
print("--------------------------------")
x =  str ( input("Escreva uma fraze: ") )
print("--------------------------------")

#Deve ignorar espaços em branco e caracteres não alfanuméricos.
x_seme_espaco = x.replace('','')

#Tornar a verificação insensível a maiúsculas e minúsculas.
x_minuscula = x_seme_espaco.lower()

#Tornar a string invertida
x_invertida = x_minuscula[::-1]


#Retorna True se a string for um palíndromo.
if x_invertida == x_minuscula:
    print(True)
    print("--------------------------------")

#Retorna False caso contrário.
else:
    print(False)
    print("--------------------------------")
