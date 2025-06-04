livro: dict = {
    "titulo":"Título do Livro",
    "autor":"Autor do Livro",
    "ano_publicacao":2020
}

lista_elementos: list = livro.items() # transforma um dicionário em uma lista
for elemento in lista_elementos:
    print(elemento)