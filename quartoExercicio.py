"""Implemente uma função que receba dois vetores (listas) de igual tamanho e retorne o
produto escalar entre eles, sem usar bibliotecas externas.
Exemplo:
A = [2, 3, 5]
B = [1, 4, 2]
→ Saída: 2*1 + 3*4 + 5*2 = 24"""

# soma dos produtos dos elementos correspondentes

A = [2, 3, 5]
B = [1, 4, 2]

def produto_escalar(A,B):
    produto_total = 0
    tamanho = len(A)
    for i in range(tamanho):
        elementoA = A[i]
        elementoB = B[i]
        produto_elementos = elementoA*elementoB
        produto_total += produto_elementos
    return produto_total

resultado = produto_escalar(A,B)
print (f"{A[0]}*{B[0]} + {A[1]}*{B[1]} + {A[2]}*{B[2]}")

print(resultado)