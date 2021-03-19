# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define uma fila encadeada
class FilaEst:
    def __init__(self, maximo):
        self.fila = [None] * maximo # define o tamanho máximo na fila dado pelo usuário
        self.max = maximo # parâmetro definido pelo o usário para o tamanho da fila
        self.primeiro = 0 # Guarda o inicio da fila
        self.final = 0 # Guarda o final da fila
        self.tamanho = 0 # guarda a quantidade de elementos da fila

    def coloca(self, elemento): # coloca elementos da fila
        if self.tamanho == self.max:
            raise IndexError("A fila está cheia")
        else:
            self.fila[self.final] = elemento
            self.final = (self.final + 1) % self.max # condição para formar uma fila circular, posição para informar o ultimo elemento 
        self.tamanho = self.tamanho + 1 

    def remove(self): # remove o primeiro elemento da fila
        if self.tamanho == 0:
            raise IndexError("A fila está vazia")
        else:
            elemento = self.fila[self.primeiro]
            self.fila[self.primeiro] == None
            self.primeiro = (self.primeiro + 1) % self.max # condição para formar uma fla circular, posição para infomrar o primeiro elemento
        self.tamanho = self.tamanho - 1
        return elemento

    def consulta(self): # informa o primeiro elemento da fila
        if self.tamanho > 0:
            return self.fila[self.primeiro]
        raise IndexError("A fila está vázia")

    def vazia(self): # infroma se a lista tá fila
        if self.tamanho == 0:
            return True
        return False

    def __del__(self): # destroi a fila
        return 0 

    def __len__(self): #informa o tamalho da fila
        return self.tamanho

    def __repr__(self): # função para representar a fila
        if self.tamanho > 0:
            aux = self.primeiro
            representacao = "["
            for i in range(0, self.tamanho):
                if aux == self.max:
                    aux = 0
                if i != self.tamanho - 1:
                    ponteiro = self.fila[aux]
                    representacao = representacao + str(ponteiro) + ", "
                else:
                    ponteiro = self.fila[aux]
                    representacao = representacao + str(ponteiro)  
                aux = aux + 1
            representacao = representacao + "]"
            return representacao
        return "Fila vazia"

    def __str__(self):
        return self.__repr__()
