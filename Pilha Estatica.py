# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define uma pilha
class PilhaEst:
    def __init__(self, maximo):
        self.topo = [None] * maximo # define o tamanho máximo na pilha dado pelo usuário
        self.max = maximo  # parâmetro definido pelo o usário para o tamanho da pilha
        self.tamanho = 0 # guarda o tamanho da pilha

    def coloca(self, elemento): # coloca um elemento na pilha
        if self.tamanho == self.max: #
            raise IndexError("Pilha está cheia")
        else:
            self.topo[self.tamanho] = elemento
        self.tamanho = self.tamanho + 1
    
    def remove(self): # remove o primeiro elemento do topo
        if self.tamanho > 0:
            elemento = self.topo[self.tamanho-1]
            self.topo[self.tamanho-1] = None
            self.tamanho = self.tamanho - 1
            return elemento
        else:
            raise IndexError("Pilha está vazia")

    def consulta(self): # informa o elemento que está no topo da pilha
        if self.tamanho > 0:
            return self.topo[self.tamanho-1]
        else:
            raise IndexError("Pilha está vazia")

    def vazia(self): # infroma se a lista tá pilha
        if self.tamanho == 0:
            return True
        return False

    def __del__(self): # destroi a pilha
        # del pilha
        return 0

    def __len__(self): # retorna com o tamanho da pilha
        # len(pilha)
        return self.tamanho
    
    def __repr__(self): # representação de uma pilha
        if self.tamanho > 0:
            representacao = " "
            i = self.tamanho - 1
            ponteiro = self.topo[i]
            while(i!=-1):
                representacao = representacao + str(ponteiro) + "\n "
                i=i-1
                ponteiro = self.topo[i] 
            return representacao
        return "Pilha vazia"

    def __str__(self):
        return self.__repr__()
