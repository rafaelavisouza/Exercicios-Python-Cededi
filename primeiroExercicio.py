"""1. Listas + Compreensão de Listas + Condicionais
Dada uma lista de números inteiros, crie um programa que gere duas listas novas.
• uma contendo apenas os números primos
• outra contendo os números não primos"""

numeros = [1, 5, 8, 2, 11, 4, 13, 9, 7, 10, 16, 3]

def primo(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False
    limite = int(n**0.5)+1  #raiz quadrada
    for i in range(3,limite,2):
        if n % i ==0:
            return False
    return True

primos = [n for n in numeros if primo(n)]
nao_primos = [ n for n in numeros if not primo(n)]

print(primos)
print(nao_primos)