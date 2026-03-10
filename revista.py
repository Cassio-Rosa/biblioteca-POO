from item_bilbioteca import Item_Biblioteca

class Revista(Item_Biblioteca):
    def __init__(self, id, titulo, ano, disponivel, edicao, mes):
        super().__init__(id, titulo, ano, disponivel)
        self.__edicao = edicao
        self.__mes = mes

    def exibir_detalhes(self):
        print(F"                 REVISTA")
        super().exibir_detalhes()
        print(f"          Edição: {self.__edicao}")   
        print(f"          Mês de Lançamento: {self.__mes}")

