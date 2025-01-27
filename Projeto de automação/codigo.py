# pip install pyautogui

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
# configurando a velocidade da execução dos comandos


# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> pressiona dus teclas de forma simultanea



# Passo 1: Abrir o sistema da empresa
#     sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# apertar tecla win
pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

# pedir pro computador esperar 3 segundos
time.sleep(3)


# Passo 2: Fazer login

pyautogui.click(x=417,y=400)


pyautogui.write("pedro@pedro.com")

# passar para o proximo campo com a tecla "tab"
pyautogui.press("tab")

pyautogui.write("PeRo@2907")

pyautogui.press("tab")

pyautogui.press("enter")


# Passo 3: Importat a base de dados dos produtos


tabela = pandas.read_csv("produto_resumido.csv")

print(tabela)


time.sleep(2)

# Passo 4: Cadastrar 1 produtos
for linha in tabela.index:

    pyautogui.click(x=397,y=288)

    # codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    pyautogui.press("enter")


    # Passo 5: Repedti o passo 4 até acabar todso os produtos
    pyautogui.scroll(10000)

