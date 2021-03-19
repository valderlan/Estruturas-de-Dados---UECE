# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# método de ordenar uma lista usando duas pilhas encadeadas
# pilhaenc é o nome do arquivo em Python que contem o codigo da Pilha Encadeada
# PilhaEnd se encontra em https://github.com/valderlan/Estruturas-de-Dados---UECE/commit/2c6796068a1fcaa1cb595021d60577099650605a

from pilhaenc import PilhaEnc # faz a chamada a classe PilhaEnd importada de pilhaend

def ordenar(lista):
  # cria duas pilhas encadeadas para fazer a ordenacao
    pi1 = PilhaEnc()
    pi2 = PilhaEnc()
    # por meio de uma variavel auxiliar eh feita a ordenacao
    aux = 0
    for i in range(len(lista)):
        pi1.coloca(lista[i])
    while (not pi1.vazia()):
        aux = pi1.remove()
        while (not pi2.vazia() and aux < pi2.consulta()):
            pi1.coloca(pi2.remove())
        pi2.coloca(aux)
    print(pi2)
# exemplo de uma lista
lista = [4,6,3,8,6,19,13,11,23,21,45]
# chamada do método 
ordenar(lista)
