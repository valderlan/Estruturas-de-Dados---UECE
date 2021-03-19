# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define um no
class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
# estrutura que define uma fila encadeada
class FilaEnc:
    def __init__(self):
        self.primeiro = None # Guarda o inicio da fila
        self.final = None # Guarda o final da fila
        self.tamanho = 0 # guarda a quantidade de elementos da fila
    

    def coloca(self, elemento): # coloca um elemento na fila
        no = No(elemento)
        if self.tamanho == 0: #caso fiSla vazia
            self.primeiro = no
            self.final = no
        else: # caso a fila não esteja vazia 
            self.final.proximo = no
            self.final = no
        self.tamanho = self.tamanho + 1

    def remove(self): # remove o primeiro elemento da fila
        if self.tamanho > 0:
            elemento = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
        else:
            raise IndexError("A fila está vázia")
        self.tamanho = self.tamanho - 1
        return elemento
   
    def consulta(self): # informa o primeiro elemento da fila
        if self.tamanho > 0:
            return self.primeiro.dado
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
            representacao = ""
            ponteiro = self.primeiro
            r = 0
            while(ponteiro):
                if r == 0:
                    representacao = representacao + str(ponteiro.dado)
                if (ponteiro != None) and (r != 0):
                    representacao = representacao + "->" + str(ponteiro.dado)
                ponteiro = ponteiro.proximo
                if ponteiro is None:
                    break
                r = 1
            return representacao
        return "Fila vazia"

    def __str__(self):
        return self.__repr__()
