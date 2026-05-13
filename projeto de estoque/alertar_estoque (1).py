def alertar_estoque_baixo(limite):
    """Identifica produtos com estoque crítico"""
    print(f"\nRELATÓRIO DE ESTOQUE BAIXO (Limite: {limite} unidades)")
    encontrou = False
    for pid, p in estoque.items():
        if p["quantidade"] < limite:
            print(f"ID: {pid} | Produto: {p['nome']} | Qtd: {p['quantidade']}")
            encontrou = True
    if not encontrou:
        print("Tudo em ordem! Nenhum produto abaixo do limite.")
