"""Receba uma lista de dicionários representando livros:
livros = [
{"titulo": "A", "ano": 2020, "preco": 45},
{"titulo": "B", "ano": 2024, "preco": 80},
{"titulo": "C", "ano": 2020, "preco": 50},
{"titulo": "D", "ano": 2022, "preco": 40}
]
Crie um programa que agrupe e mostre os livros por ano em ordem cronológica, exibindo
também o preço médio de cada ano."""

livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

def agrupar_livros_por_ano(livros):
    livros_por_ano = {}
    
    for livro in livros:
        ano = livro["ano"]
        if ano not in livros_por_ano:
            livros_por_ano[ano] = []
        livros_por_ano[ano].append(livro)
    
    return livros_por_ano

def calcular_preco_medio(livros_do_ano):
    total = sum(livro["preco"] for livro in livros_do_ano)
    return total / len(livros_do_ano)

def exibir_resultados(livros_por_ano):
    anos_ordenados = sorted(livros_por_ano.keys())
    
    for ano in anos_ordenados:
        livros_do_ano = livros_por_ano[ano]
        preco_medio = calcular_preco_medio(livros_do_ano)
        
        print(f"ANO {ano}")
        print(f"   Preço médio: R$ {preco_medio:.2f}")
        print(f"   Quantidade de livros: {len(livros_do_ano)}")
        
        for livro in livros_do_ano:
            print(f"     • '{livro['titulo']}' - R$ {livro['preco']:.2f}")



livros_agrupados = agrupar_livros_por_ano(livros)
exibir_resultados(livros_agrupados)