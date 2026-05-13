def consultar_estoque(produto_id):
    """Verifica saldo atual do produto"""
    if produto_id in estoque:
        p = estoque[produto_id]
        print(f"\n--- Detalhes do Produto (ID: {produto_id}) ---")
        print(f"Nome: {p['nome']} | Categoria: {p['categoria']}")
        print(f"Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']}")
    else:
        print("Erro: Produto não encontrado.")
