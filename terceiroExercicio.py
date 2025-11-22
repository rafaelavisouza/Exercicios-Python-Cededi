"""Crie um programa que analise o dicionário abaixo e determine qual categoria é a mais
cara em média:
produtos = {
"Alimentação": [12.50, 8.99, 15.30],
"Limpeza": [5.20, 7.80],
"Higiene": [10.00, 12.00, 9.50, 14.00]
}
O programa deve exibir:
• categoria vencedora
• média formatada com 2 casas decimais"""

produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

categoria_vencedora = " "
maior_media = -1

medias_categoria = {}

for categoria, precos in produtos.items():
    soma_total = sum(precos)
    quant = len(precos)
    media_atual = soma_total/quant
    medias_categoria[categoria] =media_atual

    if media_atual > maior_media:
        maior_media = media_atual
        categoria_vencedora = categoria

#for categoria, media in medias_categoria.items():
   # print(f"{categoria} R${media: .2f}")

media_formatada = f"{maior_media:.2f}"
print(f"Categoria Vencedora: {categoria_vencedora}")
print(f"Média Vencedora: R$ {media_formatada}")