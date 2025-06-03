# Dicionário = {chave, valor}
#**“.json** é o **dicionário** do **JavaScript”,** com algumas diferenças importantes. Por exemplo, False no JavaScript é false. Isso pode causar erros de leitura de tipos. Por exemplo, “false” poderia ser considerado uma str, e não bool.

#Dá pra converter um no outro, mas eles não são iguais.

#Em um cenário real um **Backend** pode ser feito em **Python** e um **FrontEnd** em **JavaScript**. A melhor forma dos dois se conversarem é entre **dicionário** e **.json**

import json 

produto_1: dict = {
    "nome":"sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}

produto_2: dict = {
    "nome":"tv",
    "quantidade":21,
    "preco":120,
    "disponibilidade":False
}

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

carrinho_json = json.dumps(carrinho) # converte o .json em dicionário
print(carrinho_json)