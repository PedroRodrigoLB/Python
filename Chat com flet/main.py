# Tela Inicial:
    # Título: Hashzap
    # Botão: Iniciar Chat
        # quando clicar no botão:
        # abrir um popup/modal/alerta
            # Título: Bem vindo ao Hashzap
            # Caixa de Texto: Escreva seu nome no chat 
            # Botão: Entrar no chat
                # quando clicar no botão
                # sumir com o título
                # sumir com o botão Iniciar Chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # botão enviar
                        # quando clicar no botão enviar
                        # enviar a mensagem
                        # limpar a caixa de mensagem

# Flet

# importar o Flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo
def main(pagina):
    # titulo
    titulo = ft.Text('Hashzap')

    # websocked - tunel de comunicação entre 2 usuarios
    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteça para todos os usuarios que receberam a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # criado o tunel de comunicação


    # função enviar mensagem
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"

        pagina.pubsub.send_all(mensagem) # enviar a mensagem para o tuneo de comunicação
        
        campo_enviar_mensagem.value = ""  # limpar a caixa de enviar mensagem

        pagina.update()


    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    
    chat = ft.Column()


    def entrar_chat(evento):
        # fechar o popup
        popup.open = False

        # sumir com o titulo
        pagina.remove(titulo)

        # sumir com o botão Iniciar Chat
        pagina.remove(botao) 

        # carregar o chat
        pagina.add(chat)

        # carregar o campo de enviar mensagem
        # carregar o botao enviar
        pagina.add(linha_enviar)


        # adicionar no chat a mensagem "Usuario entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # Função do botao inicial
    def abrir_popup(evento):  # o paramentro "evento" é obrigatorio quando a função criada esta associada ao click do botão
        
        pagina.dialog = popup   
        popup.open= True  # Abrir o popup
        pagina.update() 

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome", on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,actions=[botao_popup] )    

    

    # colocar os elementos na págian
    pagina.add(titulo)
    pagina.add(botao)


# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)