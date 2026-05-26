  # GESTÃO DE ESTOQUE

    Sistema de Gestão de Estoque em Python:

Este é um projeto prático desenvolvido em Python para gerenciar o inventário de produtos. O sistema permite realizar desde o cadastro inicial até o controle de entradas, saídas e alertas de reposição, utilizando uma estrutura de dicionários para armazenamento em memória.

    Funcionalidades:

O sistema oferece um menu interativo com as seguintes operações:

- Cadastrar Produto: Registra o nome, categoria, preço e quantidade inicial, gerando um ID automático para cada item.

- Registrar Entrada: Adiciona unidades ao saldo de um produto existente via ID.

- Registrar Saída: Remove unidades do estoque, com verificação automática para evitar saldo insuficiente.

- Consultar Produto: Exibe detalhes específicos de um item através do seu ID.

- Alerta de Estoque Baixo: Gera um relatório de produtos que estão abaixo de um limite mínimo definido pelo usuário.

- Visualizar Estoque Completo: Exibe uma tabela formatada com todos os itens cadastrados no sistema.

    Estrutura do Projeto:

O código foi modularizado para facilitar a manutenção e organização:

    Arquivo / Descrição:

- menu.py : Concentra a interface do usuário e o loop principal do sistema.

- cadastrar_produto.py : Lógica para inserção de novos itens e incremento do ID global.

- registrar_entrada.py : Função para somar quantidades ao estoque.

- registrar_saida.py : Função para subtrair quantidades, incluindo validação de estoque insuficiente.

- consultar_estoque.py : Busca e exibe dados individuais de um produto.

- visualizar_estoque.py : Gera o relatório tabular completo do inventário.

- alertar_estoque.py : Filtra e exibe produtos com saldo abaixo do limite de segurança.


      Tecnologias Utilizadas:
Python 3.x: Linguagem base para o desenvolvimento da lógica.

Dicionários (Dicts): Utilizados como estrutura de dados principal para armazenamento dos produtos.

Tratamento de Exceções: Uso de blocos try/except para validar que as entradas do usuário sejam numéricas.

    Como Executar:
  
Certifique-se de ter o Python instalado em sua máquina.
Clone este repositório ou baixe os arquivos.
Para que o sistema funcione corretamente, os arquivos devem estar na mesma pasta e é necessário inicializar as variáveis globais estoque e contador_id.

    Execute o arquivo do menu:
menu.py
Exemplo de Uso
Ao iniciar o programa, o menu será exibido desta forma:

==================== Sistema de Gestão de Itens ====================

Escolha umas das opções:
1. Cadastrar Produto       | 4. Consultar Produto
2. Registrar Entrada       | 5. Alerta de Estoque Baixo
3. Registrar Saída         | 6. Visualizar Estoque

Insira 0 para encerrar o programa

Este projeto foi desenvolvido como parte do meu processo de aprendizado em lógica de programação e manipulação de estruturas de dados em Python na Aula de Programação de Computadores

Alunos: Juan Gabriel Montania Lima e Arthur Rodrigues Alves
