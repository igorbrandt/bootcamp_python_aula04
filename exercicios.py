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
frutas: list = ["maçã", "banana", "cereja"]
precos_frutas: dict = {"maçã": 0.45, 
                       "banana": 0.30, 
                       "cereja": 0.65}
valor_total:float = 0
for fruta in precos_frutas:
    valor_total += precos_frutas[fruta]

print(valor_total)

### 6 Eliminação de Duplicatas. Objetivo: Dada uma lista de emails, remover todos os duplicados.
lista_emails = ["pessoa1@email.com", "pessoa1@email.com", "pessoa2@email.com", "pessoa3@email.com"]

def remover_emails_duplicados():
    lista_contagem = []

    for email in lista_emails:
        if email not in lista_contagem:
            lista_contagem.append(email)
        else:
            pass
    print(lista_contagem)

remover_emails_duplicados()

### 7. Filtragem de Dados. Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
lista_idades = [5, 6, 8, 18, 21, 44, 55, 9]

def listar_maiores_de_18():
    maiores_de_18 = []
    for idade in lista_idades:
        if idade >= 18 and idade not in maiores_de_18:
            maiores_de_18.append(idade)
        else:
            pass
    print(maiores_de_18)

listar_maiores_de_18()

### 8. Ordenação Personalizada. Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
lista_de_pessoas: list = [{"nome": "igor", "idade": 29},{"nome": "enzo", "idade":26},{"nome":"pedro", "idade":63}]
lista_de_pessoas_ordenada = sorted(lista_de_pessoas, key=lambda x: x["nome"])
print(lista_de_pessoas_ordenada)