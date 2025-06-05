## Exercícios de Listas e Dicionários
### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = []
for i in range(1, 11):
    lista.append(i**2)

print(lista)


### 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)

### 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Hipótese com diferentes dicionários, que podem ser incluídos em uma lista:
livro_1: dict = {
    "titulo":"Título do Livro",
    "autor":"Autor do Livro",
    "ano":2020
}

livro_2: dict = {
    "titulo":"Título do Livro 2",
    "autor":"Autor do Livro 2",
    "ano":2015
}

lista_de_livros = []
lista_de_livros.append(livro_1)
lista_de_livros.append(livro_2)  
# print(lista_de_livros)

# Hipótese com dicionário de dicionários
lista_de_livros_dict: dict = {
    "livro_1":{"titulo":"Título do Livro",
    "autor":"Autor do Livro",
    "ano":2020},

    "livro_2":{"titulo":"Título do Livro 2",
    "autor":"Autor do Livro 2",
    "ano":2015}
}

def listar_livros():
    lista_elementos: list = lista_de_livros_dict.items() # transforma um dicionário em uma lista
    for elemento in lista_elementos:
        print(elemento)

listar_livros()

print(lista_de_livros_dict["livro_1"])
print(lista_de_livros_dict["livro_1"]["titulo"])

### 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

frase = "Comprei um limão e um abcaaxi.."
print(contar_caracteres(frase))

### 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.