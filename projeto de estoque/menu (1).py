def menu():
    while True:
        print("\n==================== Sistema de Gestão de Itens ====================")
        print("\nEscolha umas das opções:")
        print("1. Cadastrar Produto       | 4. Consultar Produto")
        print("2. Registrar Entrada       | 5. Alerta de Estoque Baixo")
        print("3. Registrar Saída         | 6. Visualizar Estoque")
        print("\nInsira 0 para encerrar o programa")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome do produto: ")
                cat = input("Categoria: ")
                preco = float(input("Preço: "))
                qtd = int(input("Quantidade inicial: "))
                cadastrar_produto(nome, cat, preco, qtd)

            elif opcao == "2":
                pid = int(input("ID do produto: "))
                qtd = int(input("Quantidade a adicionar: "))
                registrar_entrada(pid, qtd)

            elif opcao == "3":
                pid = int(input("ID do produto: "))
                qtd = int(input("Quantidade a retirar: "))
                registrar_saida(pid, qtd)

            elif opcao == "4":
                pid = int(input("ID do produto: "))
                consultar_estoque(pid)

            elif opcao == "5":
                limite = int(input("Defina o limite mínimo: "))
                alertar_estoque_baixo(limite)

            elif opcao == "6":
                visualizar_estoque_completo()

            elif opcao == "0":
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos.")
