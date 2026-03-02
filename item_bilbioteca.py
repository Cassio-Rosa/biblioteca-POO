class Item_Biblioteca():
    def __init__(self, id: int, titulo: str, ano: int, disponivel: bool):
        self.__id = id
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"""

           ID: {self.__id}
           Titulo: {self.__titulo}
           Ano de lançamento: {self.__ano}
           Disponibilidade: {self.__disponivel}
        """)

    def set_emprestar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            print(f"Obra {self.__titulo} emprestada com sucesso")
        else:
            print(f"Não pode pegar um livro que ja foi emprestado")

    def set_devolver(self):
        if self.__disponivel == False:
            self.__disponivel = True
            print(f"Obra {self.__titulo} devolvida com sucesso")
        else:
            print(f"Não pode devolver um livro que não foi emprestado")

    
