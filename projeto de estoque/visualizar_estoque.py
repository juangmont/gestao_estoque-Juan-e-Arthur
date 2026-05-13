def visualizar_estoque_completo():
    """Exibe todos os produtos cadastrados em formato de tabela"""
    if not estoque:
        print("\n--- O estoque está vazio! ---")
        return

    print("\n" + "="*70)
    print(f"{'ID':<5} | {'NOME':<20} | {'CATEGORIA':<15} | {'PREÇO':<10} | {'QTD':<5}")
    print("-" * 70)

    for produto_id, dados in estoque.items():
        nome = dados['nome']
        cat = dados['categoria']
        preco = f"R${dados['preco']:.2f}"
        qtd = dados['quantidade']
        
        print(f"{produto_id:<5} | {nome:<20} | {cat:<15} | {preco:<10} | {qtd:<5}")
    
    print("="*70)
