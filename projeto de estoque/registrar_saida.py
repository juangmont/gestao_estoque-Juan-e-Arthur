def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""
    if produto_id in estoque:
        if estoque[produto_id]["quantidade"] >= quantidade:
            estoque[produto_id]["quantidade"] -= quantidade
            print(f"Saída registrada! Novo saldo de {estoque[produto_id]['nome']}: {estoque[produto_id]['quantidade']}")
        else:
            print("Erro: Estoque insuficiente para esta operação.")
    else:
        print("Erro: Produto não encontrado.")
