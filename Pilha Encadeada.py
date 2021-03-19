# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define um no
class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
# estrutura que define uma pilha
class PilhaEnc:
    def __init__(self):
        self.topo = None # guarda o topo da pilha
        self.tamanho = 0 # guarda a quantidade de elementos da pilha

    def coloca(self, elemento): # coloca um elemento na pilha
        no = No(elemento)
        if self.tamanho == 0: # coloca o primeiro elemento na pilha
            self.topo = no
        else: # coloca o proximo elemento em cima do primeiro
            no.proximo = self.topo
            self.topo = no
        self.tamanho = self.tamanho + 1
    
    def remove(self): # remove o primeiro elemento do topo
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho = self.tamanho - 1
            return no.dado
        else:
            raise IndexError ("Pilha está vazia")

    def consulta(self): # informa o elemento que está no topo da pilha
        if self.tamanho > 0:
            return self.topo.dado
        else:
            raise IndexError("Pilha está vazia")

    def vazia(self): # infroma se a lista tá pilha
        if self.tamanho == 0:
            return True
        return False

    def __del__(self): # destroi a pilha
        # del pilha
        return 0

    def __len__(self): # informa o a quantidade de elementos na pilha
        # len(pilha)
        return self.tamanho
    
    def __repr__(self): # representação de uma pilha
        if self.tamanho > 0:
            representacao = ""
            ponteiro = self.topo
            while(ponteiro):
                representacao = representacao + str(ponteiro.dado) + "\n"
                ponteiro = ponteiro.proximo
            return representacao
        return "Pilha vázia"

    def __str__(self):
        return self.__repr__()
