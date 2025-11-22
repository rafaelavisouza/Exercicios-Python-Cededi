"""Você recebe uma lista de tuplas contendo (nome, nota) de alunos.
Crie um programa que:
• transforme os dados em um dicionário
• se o aluno já existir, calcule a média das notas recebidas
• exiba os alunos em ordem crescente de média
Exemplo de entrada:
[("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]"""

lista = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

notas_agrupadas = {}

for nome, nota in lista:
    if nome in notas_agrupadas:
        notas_agrupadas[nome].append(nota)
    else:
        notas_agrupadas[nome] = [nota]

#print(notas_agrupadas)

medias_finais = {}

for nome, lista_de_notas in notas_agrupadas.items():
    soma_total = sum(lista_de_notas)
    contagem = len(lista_de_notas)
    media=soma_total/contagem
    medias_finais[nome]=media

#print(medias_finais)

lista_ordem = list(medias_finais.items())

alunos_ordem = sorted(lista_ordem,key=lambda item: item[1]) #key: ordenar a lista não pelo primeiro elemento 

for nome, media in alunos_ordem:
    print(f"Aluno: {nome} Média: {media}")