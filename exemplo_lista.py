produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "calça"

produtos = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

produtos.remove(produto_2)
produtos.pop()  # Remove o último item adicionado. Melhor performance, pois não precisa criar uma consulta

print(produtos)
