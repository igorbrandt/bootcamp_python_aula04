import csv

path: str = "C:\\Users\\Igor\\Documents\\Programação\\jornada_de_dados\\bootcamp_python_aula04\\exemplo.csv"

# Criar uma lista para incluir dicionários entro dela. 
# Cada linha do csv vai ser um dicionário.
arquivo_csv: list = [] 

# Abrir o arquivio csv
with open(file=path, mode="r", encoding="utf-8") as arquivo:
    # Gera um arquivo binário Não é possível trabalhar com ele. Não posso printar, por ex.
    leitor_csv = csv.DictReader(arquivo)
    
     # Preciso jogar cada linha do arquivo para uma lista:
    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)

