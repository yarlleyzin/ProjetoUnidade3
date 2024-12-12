from Funções import *
import os
import matplotlib.pyplot as plt

os.system('pip install matplotlib')

print('-----BEM VINDO AO FESTIVAL DE EVENTOS!-----')


usuario_logado = None
while True:
    print('\nESCOLHA SUA FUNÇÃO!\n')
    print('1 - Cadastrar novo participante')
    print('2 - Cadastrar administrador')
    print('3 - Login')
    print('4 - Avaliar evento')
    print('5 - Ver média de avaliações de um evento')
    print('6 - Cadastrar evento')
    print('7 - Listar eventos')
    print('8 - Buscar evento')
    print('9 - Remover evento')
    print('10 - Participar de evento')
    print('11 - Listar participantes do evento')
    print('12 - Verificar valor arrecadado')
    print('13 - Adicionar participante ao evento')
    print('14 - Listar todos os participantes do evento')
    print('15 - Gerar gráfico de barra com quantidade de participantes dos eventos')
    print('16 - Listar todos os participantes e salvar em arquivo .txt')
    print('17 - Listar usuários proibidos (menores de 12 anos)')
    print('0 - Fechar programa')

    escolha = input('Digite o que você deseja: ')
    if not escolha.isdigit():
        print('Opção inválida! Digite um número.')
        continue

    escolha = int(escolha)

    if escolha == 0:
        print('Programa encerrado.')
        break
    elif escolha == 17:
        listar_usuarios_proibidos()
    elif escolha == 1:
        nome = input('Digite seu nome: ')
        email = verificar_email(input('Digite seu E-mail: '))
        senha = verificar_senhas(input('Digite sua senha: '), input('Digite sua senha novamente: '))
        if verificar_idade():
            cadastrar_usuario(nome, email, senha)
    elif escolha == 2:
        nome = input('Digite seu nome: ')
        email = verificar_email(input('Digite seu E-mail: '))
        senha = verificar_senhas(input('Digite sua senha: '), input('Digite sua senha novamente: '))
        cadastrar_usuario(nome, email, senha, 'administrador')
    elif escolha == 3:
        email = input('Digite seu E-mail: ')
        senha = input('Digite sua senha: ')
        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                usuario_logado = usuario
                print(f'Olá, {usuario["nome"]}, você entrou no sistema!')
                break
        if not usuario_logado:
            print('Email ou senha incorretos.')
    elif escolha == 4:
        if usuario_logado and usuario_logado['tipo'] == 'participante':
            nome_evento = input('Digite o nome do evento que deseja avaliar: ')
            nota = int(input('Digite uma nota de 1 a 5 para o evento: '))
            if nota < 1 or nota > 5:
                print('Nota inválida. Digite uma nota entre 1 e 5.')
            else:
                inscricoes.append({'usuario': usuario_logado['nome'], 'evento': nome_evento, 'nota': nota})
                print('Avaliação realizada com sucesso!')
        else:
            print('Somente participantes podem avaliar eventos.')
    elif escolha == 5:
        nome_evento = input('Digite o nome do evento para verificar a média de avaliações: ')
        verificar_media_avaliacao(nome_evento)
    elif escolha == 6:
        if usuario_logado and usuario_logado['tipo'] == 'administrador':
            nome_evento = input('Digite o nome do evento: ')
            local = input('Digite o local do evento: ')
            data = input('Digite a data do evento (DD/MM/AAAA): ')
            ingressos = input('Digite o número de ingressos: ')
            descricao = input('Digite uma descrição para o evento: ')
            preco = input('Digite o preço do ingresso: ')
            cadastrar_evento(nome_evento, local, data, ingressos, descricao, preco, usuario_logado['nome'])
        else:
            print('Apenas administradores podem cadastrar eventos.')
    elif escolha == 7:
        listar_eventos()
    elif escolha == 8:
        nome_evento = input('Digite o nome do evento que você deseja buscar: ')
        buscar_evento(nome_evento)
    elif escolha == 9:
        if usuario_logado and usuario_logado['tipo'] == 'administrador':
            nome_evento = input('Digite o nome do evento que deseja remover: ')
            remover_evento(nome_evento, usuario_logado['nome'])
        else:
            print('Apenas administradores podem remover eventos.')
    elif escolha == 10:
        if usuario_logado and usuario_logado['tipo'] == 'participante':
            nome_evento = input('Digite o nome do evento que deseja participar: ')
            participar_evento(nome_evento, usuario_logado['nome'])
        else:
            print('Somente participantes podem se inscrever em eventos.')
    elif escolha == 11:
        if usuario_logado and usuario_logado['tipo'] == 'administrador':
            nome_evento = input('Digite o nome do evento para listar participantes: ')
            listar_participantes_evento(nome_evento, usuario_logado['nome'])
        else:
            print('Apenas administradores podem listar participantes de eventos.')
    elif escolha == 12:
        if usuario_logado and usuario_logado['tipo'] == 'administrador':
            nome_evento = input('Digite o nome do evento para verificar o valor arrecadado: ')
            verificar_valor_arrecadado(nome_evento, usuario_logado['nome'])
        else:
            print('Apenas administradores podem verificar o valor arrecadado dos eventos.')
    elif escolha == 13:
        if usuario_logado and usuario_logado['tipo'] == 'administrador':
            nome_evento = input('Digite o nome do evento para adicionar um participante: ')
            adicionar_participante(nome_evento)
        else:
            print('Apenas administradores podem adicionar participantes a eventos.')
    elif escolha == 14:
        listar_todos_participantes()
    elif escolha == 15:
        if not eventos:
            print('Nenhum evento cadastrado.')
        else:
            nomes_eventos = [evento['nome'] for evento in eventos]
            participantes_eventos = [sum(1 for inscricao in inscricoes if inscricao['evento'] == evento['nome']) for evento in eventos]
            plt.bar(nomes_eventos, participantes_eventos)
            plt.xlabel('Eventos')
            plt.ylabel('Número de Participantes')
            plt.title('Número de Participantes por Evento')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
    elif escolha == 16:
        salvar_participantes_em_arquivo()
    else:
        print('Opção inválida! Tente novamente.')
