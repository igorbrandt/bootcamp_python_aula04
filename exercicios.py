## Exercícios de Listas e Dicionários
# %%
### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = []
for i in range(1, 11):
    lista.append(i**2)

print(lista)

# %%
### 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)

# %%
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

# %%
### 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

frase = "Comprei um limão e um abcaaxi.."
print(contar_caracteres(frase))

# %%
### 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
frutas: list = ["maçã", "banana", "cereja"]
precos_frutas: dict = {"maçã": 0.45, 
                       "banana": 0.30, 
                       "cereja": 0.65}
valor_total:float = 0
for fruta in precos_frutas:
    valor_total += precos_frutas[fruta]

print(valor_total)

# %%
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

# %%
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

# %%
### 8. Ordenação Personalizada. Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
lista_de_pessoas: list = [{"nome": "igor", "idade": 29},{"nome": "enzo", "idade":26},{"nome":"pedro", "idade":63}]
lista_de_pessoas_ordenada = sorted(lista_de_pessoas, key=lambda x: x["nome"])
print(lista_de_pessoas_ordenada)

# %%
### 9. Agregação de Dados. Objetivo: Dado um conjunto de números, calcular a média.
numeros = [1, 8]
media = sum(numeros) / len(numeros)
print(media)

# %%
### 10. Divisão de Dados em Grupos. Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 0]
numeros_pares = []
numeros_impares = []

def identificar_numeros_pares_e_impares():
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    print(f"Números Pares: {numeros_pares}")
    print(f"Números Ímpares: {numeros_impares}")

identificar_numeros_pares_e_impares()

# %%
### 11. Atualização de Dados. Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
precos_produtos: dict = {"óleo": 2.39, 
                       "desodorante": 15.20, 
                       "cortina": 1200.99}

def atualizar_preco_do_produto():
    produto = input("Digite o produto que deseja atualizar o preço: ")
    novo_preco = input("Digite o novo preço do produto: ")
    precos_produtos[produto] = novo_preco
    print(precos_produtos)

atualizar_preco_do_produto()

# %%
### 12. Fusão de Dicionários. Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
parametros_igor = {"igor": 29}
parametros_enzo = {"enzo": 26}
parametros_totais = parametros_igor | parametros_enzo
print(parametros_totais)

# %%
### 13. Filtragem de Dados em Dicionário. Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

def mostrar_produtos_com_quantidade_positiva():
    estoque_positivo = {}
    for produto, quantidade in estoque.items():
        if quantidade > 0:  # Filtra apenas os produtos com quantidade maior que zero
            estoque_positivo[produto] = quantidade  # Adiciona ao novo dicionário
    print(estoque_positivo)

mostrar_produtos_com_quantidade_positiva()

# %%
### 14. Extração de Chaves e Valores. Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())
print(chaves)
print(valores)

# %%
### 15. Contagem de Frequência de Itens. Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
string = "Cheguei da escola e fui jogar bola na pracinha"

def contar_numero_de_caracteres():
    string_lower = string.lower()
    caracteres = {}
    for caractere in string_lower:
        if caractere in caracteres:
            caracteres[caractere] += 1
        else:
            caracteres[caractere] = 1
    print(caracteres)

contar_numero_de_caracteres()

# %%
### 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def somar_numeros():
    somatorio_total = 0
    lista_de_numeros: list = (input("Digite uma lista de números separados por vírgula: "))
    lista_de_numeros_individuais = [float(num) for num in lista_de_numeros.split(",")]
    for numero in lista_de_numeros_individuais:
        somatorio_total = numero + somatorio_total

    print(somatorio_total)

somar_numeros()

# %%
### 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def eh_numero_primo(numero):
    if numero < 2: # Números menores que 2 não são primos
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Testa divisores até a raiz quadrada
        if numero % i == 0:  # Se for divisível por outro número, não é primo
            return False
    return True  # Se passou no teste, é primo

num = int(input("Digite um número inteiro: "))
if eh_numero_primo(num):
    print(f"{num} é um número primo. ")
else:
    print(f"{num} não é um número primo. ")

# %%
### 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverter_string_de_texto(string):
    string_revertida = ''.join(reversed(string))
    return string_revertida

texto = input("Digite um texto para ser revertido: ")
print(reverter_string_de_texto(texto))

# %%
### 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_pares(lista, alvo):
    pares = []
    
    # Percorre a lista pegando cada número
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # Evita pares repetidos
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))  # Adiciona o par na lista
    
    return pares

# Testando
numeros = [1, 2, 3, 4, 5, 6]
alvo = 7
print(encontrar_pares(numeros, alvo))

# %%
### 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
dicionario: dict = {"nome":"igor","idade":29,"altura":1.74}

def listar_de_chaves(dicionario):
    lista_de_chaves = sorted(dicionario.keys())
    return lista_de_chaves
    
print(listar_de_chaves(dicionario))

# %%
