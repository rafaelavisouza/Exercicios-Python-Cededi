"""Faça um programa que receba um número digitado pelo usuário e:
• verifique se pode ser convertido para float
• caso não possa, exiba uma mensagem de erro personalizada
• se o número for válido:
o se for decimal (ex.: 2.5), exiba sua parte inteira e decimal
o se for inteiro, informe se é par ou ímpar"""

numero = input("digite um númeoro ")

def converter_float(numero):
    try:
        return float(numero)
    except ValueError:
        return None
    
def analise():
    numero_val = converter_float(numero)
    if numero_val is None:
        print(f"'{numero}' não é um número válido.")
        return
    print(f"Número recebido: {numero_val}")

    if numero_val == int(numero_val):
        print("Tipo inteiro")
        numero_int = int(numero_val)
        if numero_int%2==0:
            print(f"Número {numero_int} é PAR.")
        else:
            print(f"Número {numero_int} é ÍMPAR.")
    else: 
        print("Tipo decimal")
        parte_int = int(numero_val)
        parte_dec = numero_val - parte_int

        print(f"Parte Inteira = {parte_int}")
        print(f"Parte Decimal = {parte_dec:.6f}")
analise()