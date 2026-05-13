def registrar_entrada(produto_id, quantidade):
    """Adiciona itens ao estoque"""
    if produto_id in estoque:
        estoque[produto_id]["quantidade"] += quantidade
        print(f"Entrada registrada! Novo saldo de {estoque[produto_id]['nome']}: {estoque[produto_id]['quantidade']}")
    else:
        print("Erro: Produto não encontrado.")
