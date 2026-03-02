from item_bilbioteca import Item_Biblioteca as IB

class Livro(IB):
    def __init__(self, id, titulo, ano, disponivel, autor, num_pag):
        super().__init__(id, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_pg = num_pag

    def exibir_detalhes(self):
        print(F"                 LIVRO")
        super().exibir_detalhes()
        print(f"          Autor: {self.__autor}")   
        print(f"          Numero de Paginas: {self.__num_pg}")   


