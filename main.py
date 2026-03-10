from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

biblioteca = Biblioteca()

while True:

    print(f"""
                BIBLIOTECA

        1 - Cadastrar Livro 
        2 - Cadastrar Revista
        3 - Listar Itens
        4 - Emprestar Item
        5 - Devolver Item
        6 - Sair
    """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        id = int(input("ID: "))
        titulo = input("Titulo: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        paginas = int(input("Numero de paginas: "))

        livro = Livro(id, titulo, ano, True, autor, paginas)

        biblioteca.adicionar_item(livro)

        print(f"Livro {titulo} cadastrado com sucesso")

    elif opcao == "2":

        id = int(input("ID: "))
        titulo = input("Titulo: ")
        ano = int(input("Ano: "))
        edicao = int(input("Edicao: "))
        mes = input("Mes: ")

        revista = Revista(id, titulo, ano, True, edicao, mes)

        biblioteca.adicionar_item(revista)

        print(f"Revista {titulo} cadastrada com sucesso")

    elif opcao == "3":

        biblioteca.listar_itens()

    elif opcao == "4":

        codigo = int(input("Codigo do item: "))
        biblioteca.emprestar_item(codigo)

    elif opcao == "5":

        codigo = int(input("Codigo do item: "))
        biblioteca.devolver_item(codigo)

    elif opcao == "6":

        print(f"Encerrando sistema")
        break

    else:

        print(f"Opcao invalida")