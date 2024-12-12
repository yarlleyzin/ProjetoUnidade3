
usuarios = []
eventos = []
inscricoes = []
usuarios_proibidos = []


def verificar_email(email):
    while "@" not in email or len(email) < 5:
        if "@" not in email:
            print('Esse Email não contém "@". Por favor, digite um E-mail válido:')
        if len(email) < 5:
            print('Esse Email deve ter pelo menos 5 caracteres. Por favor, digite um E-mail válido:')
        email = input('Digite seu E-mail: ')
    for usuario in usuarios:
        if usuario['email'] == email:
            print('Esse Email já pertence a um usuário. Por favor, digite um Email diferente!')
            email = input('Digite seu E-mail: ')
            return verificar_email(email)
    return email


def verificar_senhas(senha1, senha2):
    while senha1 != senha2 or len(senha1) < 4:
        if senha1 != senha2:
            print('Senhas não correspondem, digite novamente!')
        if len(senha1) < 4:
            print('A senha deve ter pelo menos 4 caracteres. Por favor, digite novamente!')
        senha1 = input('Digite sua senha: ')
        senha2 = input('Digite sua senha novamente: ')
    print('Senha aceita com sucesso!')
    return senha1


def verificar_idade():
    idade = int(input('Digite sua idade: '))
    if idade < 12:
        print('Usuários menores de 12 anos não podem ser cadastrados.')
        usuarios_proibidos.append({'nome': input('Digite seu nome: '), 'idade': idade})
        return False
    return True


def cadastrar_usuario(nome, email, senha, tipo='participante'):
    usuarios.append({'nome': nome, 'email': email, 'senha': senha, 'tipo': tipo})
    print(f'Usuário {nome} cadastrado com sucesso como {tipo}!')


def cadastrar_evento(nome_evento, local, data, ingressos, descricao, preco, criador):
    eventos.append({
        'nome': nome_evento,
        'local': local,
        'data': data,
        'ingressos': int(ingressos),
        'descricao': descricao,
        'preco': float(preco),
        'criador': criador
    })
    print('Evento cadastrado com sucesso!')


def listar_eventos():
    if not eventos:
        print('Nenhum evento cadastrado.')
    else:
        print('\nLista de Eventos:')
        for i, evento in enumerate(eventos, start=1):
            print(f"{i}. Nome: {evento['nome']}, Local: {evento['local']}, Data: {evento['data']}, "
                  f"Ingressos: {evento['ingressos']}, Descrição: {evento['descricao']}, "
                  f"Preço: R${evento['preco']:.2f}")


def buscar_evento(nome_evento):
    encontrado = False
    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            print(f"Evento encontrado: Nome: {evento['nome']}, Local: {evento['local']}, "
                  f"Data: {evento['data']}, Ingressos: {evento['ingressos']}, "
                  f"Descrição: {evento['descricao']}, Preço: R${evento['preco']:.2f}")
            encontrado = True
    if not encontrado:
        print('Evento não encontrado.')


def remover_evento(nome_evento, criador):
    for evento in eventos:
        if evento['nome'] == nome_evento and evento['criador'] == criador:
            eventos.remove(evento)
            print('Evento removido com sucesso!')
            return
    print('Evento não encontrado ou você não tem permissão para removê-lo.')


def participar_evento(nome_evento, usuario):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            if evento['ingressos'] > 0:
                inscricoes.append({'usuario': usuario, 'evento': nome_evento})
                evento['ingressos'] -= 1
                print(f'Inscrição realizada com sucesso no evento: {nome_evento}')
            else:
                print('Ingressos esgotados para este evento.')
            return
    print('Evento não encontrado.')


def listar_participantes_evento(nome_evento, criador):
    for evento in eventos:
        if evento['nome'] == nome_evento and evento['criador'] == criador:
            print(f'Participantes do evento "{nome_evento}":')
            participantes = [inscricao['usuario'] for inscricao in inscricoes if inscricao['evento'] == nome_evento]
            if participantes:
                for participante in participantes:
                    print(participante)
            else:
                print('Nenhum participante inscrito.')
            return
    print('Evento não encontrado ou você não tem permissão para listar os participantes.')


def verificar_valor_arrecadado(nome_evento, criador):
    for evento in eventos:
        if evento['nome'] == nome_evento and evento['criador'] == criador:
            participantes = [inscricao for inscricao in inscricoes if inscricao['evento'] == nome_evento]
            total_arrecadado = len(participantes) * evento['preco']
            print(f"Total arrecadado: R${total_arrecadado:.2f}, Número de inscritos: {len(participantes)}")
            return
    print('Evento não encontrado ou você não tem permissão para ver o valor arrecadado.')


def verificar_usuario_proibido(nome):
    for usuario in usuarios_proibidos:
        if usuario['nome'] == nome:
            return True
    return False


def adicionar_participante(nome_evento):
    nome = input('Digite o nome do participante: ')
    if verificar_usuario_proibido(nome):
        print(f'O usuário {nome} está proibido de participar deste evento.')
        return
    for evento in eventos:
        if evento['nome'] == nome_evento:
            inscricoes.append({'usuario': nome, 'evento': nome_evento})
            print(f'Usuário {nome} adicionado ao evento {nome_evento} com sucesso!')
            return
    print('Evento não encontrado.')


def listar_todos_participantes():
    if not eventos:
        print('Nenhum evento cadastrado.')
    else:
        participantes = []
        for evento in eventos:
            for inscricao in inscricoes:
                if inscricao['evento'] == evento['nome']:
                    participantes.append({
                        'evento': evento['nome'],
                        'participante': inscricao['usuario']
                    })
        if participantes:
            print('\nLista de Todos os Participantes:')
            for participante in participantes:
                print(f"Evento: {participante['evento']}, Participante: {participante['participante']}")


def salvar_participantes_em_arquivo():
    with open('participantes.txt', 'w') as file:
        for inscricao in inscricoes:
            file.write(f"Evento: {inscricao['evento']}, Participante: {inscricao['usuario']}\n")
    print('Lista de participantes salva em participantes.txt.')


def verificar_media_avaliacao(nome_evento):
    encontrado = False
    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower():
            avaliacoes = [inscricao['nota'] for inscricao in inscricoes if inscricao['evento'] == nome_evento]
            if avaliacoes:
                media = sum(avaliacoes) / len(avaliacoes)
                print(f'Média de avaliações para o evento "{nome_evento}": {media:.2f} estrelas')
            else:
                print('Nenhuma avaliação encontrada para este evento.')
            encontrado = True
            break
    if not encontrado:
        print('Evento não encontrado.')



def listar_usuarios_proibidos():
    if not usuarios_proibidos:
        print('Nenhum usuário proibido.')
    else:
        print('\nLista de Usuários Proibidos (menores de 12 anos):')
        for usuario in usuarios_proibidos:
            if usuario['idade'] < 12:
                print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")
