def atualizar(nomes):
    nome_cliente = input("Nome do cliente: ")
    if(nome_cliente in nomes):
        posicao = nomes.index(nome_cliente)
        novo_nome = input("Novo nome: ")
        nomes[posicao] = novo_nome
