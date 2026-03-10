# Sistema de Biblioteca - POO

Projeto desenvolvido em **Python** com o objetivo de simular um sistema simples de gerenciamento de itens de uma biblioteca, permitindo o cadastro, listagem, empréstimo e devolução de livros e revistas.

O projeto foi criado para praticar conceitos de **Programação Orientada a Objetos (POO)**, como encapsulamento, herança e polimorfismo.

---

## Estrutura do Projeto

```
biblioteca-poo/

README.md
main.py
biblioteca.py
item_biblioteca.py
livro.py
revista.py
```

### Arquivos

**item_biblioteca.py**

Classe base do sistema.
Define os atributos comuns a todos os itens da biblioteca.

Atributos:

* id
* titulo
* ano
* disponivel

Métodos:

* exibir_detalhes()
* emprestar()
* devolver()

---

**livro.py**

Classe que representa um livro na biblioteca.
Herda de `Item_Biblioteca`.

Atributos extras:

* autor
* numero de paginas

Sobrescreve o método:

* exibir_detalhes()

---

**revista.py**

Classe que representa uma revista na biblioteca.
Herda de `Item_Biblioteca`.

Atributos extras:

* edicao
* mes

Sobrescreve o método:

* exibir_detalhes()

---

**biblioteca.py**

Classe responsável por controlar os itens cadastrados na biblioteca.

Funcionalidades:

* adicionar itens
* listar itens
* buscar item por código
* emprestar item
* devolver item

---

**main.py**

Arquivo principal do programa.
Contém o menu interativo no terminal para interação com o usuário.

---

## Funcionalidades

O sistema permite:

* Cadastrar livros
* Cadastrar revistas
* Listar todos os itens cadastrados
* Emprestar um item da biblioteca
* Devolver um item emprestado

---

## Conceitos de POO utilizados

**Encapsulamento**

* Uso de atributos privados com `__atributo`.

**Herança**

* `Livro` e `Revista` herdam de `Item_Biblioteca`.

**Polimorfismo**

* O método `exibir_detalhes()` é sobrescrito nas subclasses.

---

## Como executar o projeto

1. Baixe ou clone o repositório

```
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto

```
cd biblioteca-poo
```

3. Execute o programa

```
python main.py
```

---

## Exemplo de uso

Menu do sistema:

```
1 - Cadastrar Livro
2 - Cadastrar Revista
3 - Listar Itens
4 - Emprestar Item
5 - Devolver Item
6 - Sair
```

O usuário pode interagir com o sistema digitando a opção desejada.

---

## Autor

Projeto desenvolvido por **Cassio Rosa** para prática de Programação Orientada a Objetos em Python.
