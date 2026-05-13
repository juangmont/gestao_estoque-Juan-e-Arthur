def cadastrar_produto(nome, categoria, preco, quantidade):
    """Registra novo produto no sistema"""
    global contador_id
    estoque[contador_id] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }
    print(f"\nProduto '{nome}' cadastrado com ID {contador_id}!")
    contador_id += 1
