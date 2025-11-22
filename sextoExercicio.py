"""Usando Counter da biblioteca collections, escreva um programa que receba uma frase do
usuário e exiba:
• o 3° caractere mais frequente
• e quantas vezes ele aparece
Caso hajam empates ou menos de 3 caracteres únicos, trate adequadamente com
mensagens claras."""

from collections import Counter

frase_usuario = input("Digite uma frase: ")

def encontrar_terceiro (frase_usuario):
    frase_clean= "".join(frase_usuario.split()).lower()
    contagem = Counter(frase_clean)
    top_tres = contagem.most_common(3)
    if len(top_tres)<3:
        print(f"Não foi possível determinar o 3º caractere mais frequente. A frase contém apenas {len(top_tres)} caractere(s) único(s)")
    terceiro_caractere = top_tres[2][0]
    frequencia = top_tres [2][1]
    
    freq_seg = top_tres[1][1]
    if frequencia == freq_seg:
        print("Há um empate entre 2° e 3° caractere")
    print(f"3º caractere mais frequente é: '{terceiro_caractere}'. Ele aparece: {frequencia} vez(es)")

encontrar_terceiro(frase_usuario)