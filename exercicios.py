## Exercícios de Listas e Dicionários
# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = []
for i in range(1, 11):
    lista.append(i**2)

print(lista)


# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
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

lista_elementos: list = livro.items() # transforma um dicionário em uma lista
for elemento in lista_elementos:
    print(elemento)


