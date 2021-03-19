# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define um no
class No: 
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
# estrutura que define uma lista encadeada
class ListaEnc: 
    def __init__(self):
        self.inicio = None # guarda o inicio da lista
        self.tamanho = 0 # guarda o tamanho da lista

    def addF(self, elemento): # add um elemento no final da lista
        no = No(elemento)
        if self.inicio: #  insere elemento no final da lista quando já tem um elemento
            ponteiro = self.inicio
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = no
        else: # insere o primeiro elemento na lista
            self.inicio = no
        self.tamanho = self.tamanho + 1
    
    def addI(self,elemento): # add um elemento no inicio da lista
        no = No(elemento)
        if self.inicio:
            no.proximo = self.inicio
            self.inicio = no
        else: # insere o primeiro elemento na lista
            self.inicio = no
        self.tamanho = self.tamanho + 1

    def _getno(self, indice): # informa a posiçao do no onde se deseja encontrar
        ponteiro = self.inicio # a busca se inicia no primeiro elemento
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("Indice fora da lista")
        return ponteiro

    def inserir(self, indice, elemento): # insere o elemento de acordo com o indice informado
        no = No(elemento)
        if indice == 0:
            self.addI(elemento)
        elif indice == self.tamanho:
            self.addF(elemento)
        elif indice > self.tamanho:
            raise IndexError("indice fora da lista")
        else:
            ponteiro = self._getno(indice-1)
            no.proximo = ponteiro.proximo # guarda a ligação que estava entre os elementos
            ponteiro.proximo = no # insere o elemento na posição
            self.tamanho = self.tamanho + 1

    def delI(self): # deleta o primeiro elemento da lista
        if self.vazia():
            raise IndexError("A lista está vazia")
        elif self.tamanho == 1:
            self.inicio = None
        else:
            self.inicio = self.inicio.proximo
        self.tamanho = self.tamanho - 1

    def delF(self):
        if self.vazia():
            raise IndexError("A lista está vazia")
        elif self.tamanho == 1:
            self.inicio = None
        else:
            ponteiro = self.inicio
            while(True):
                if ponteiro.proximo.proximo == None:
                    break
                ponteiro = ponteiro.proximo
            ponteiro.proximo = None
        self.tamanho = self.tamanho - 1

    def indice(self, elemento):
        ponteiro = self.inicio
        i=0
        while(ponteiro):
            if ponteiro.dado == elemento:
                return i
            ponteiro = ponteiro.proximo
            i = i + 1
        raise ValueError("{} não tá na lista".format(elemento))
    
    def delete(self,elemento): # deleta a primeira ocorrencia de um elemento na lista
        if self.inicio == None:
            raise ValueError("{} não tá na lista".format(elemento))
        elif self.inicio.dado == elemento:
            self.inicio = self.inicio.proximo
            self.tamanho = self.tamanho - 1
            return True
        else:
            anterior = self.inicio
            ponteiro = self.inicio.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    anterior.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                anterior = ponteiro
                ponteiro = ponteiro.proximo
            self.tamanho = self.tamanho - 1
            return True
        raise ValueError("{} não tá na lista".format(elemento))
    
    def delind(self, indice): # função de remove o elemento do indice solicitado na lista
        if self.tamanho == 0:
            self.vazia()
        if indice > self.tamanho:
            raise IndexError("Indide fora da lista")
        elif indice == 0:
            elemento = self.inicio.dado
            self.inicio = self.inicio.proximo
        else:
            ponteiro = self._getno(indice-1)
            elemento = ponteiro.proximo.dado
            ponteiro.proximo = ponteiro.proximo.proximo
        self.tamanho = self.tamanho - 1

    def vazia(self): # infroma se a lista tá vazia 
        if self.tamanho == 0:
            return True
        return False

    def limpar(self): # função para limpar toda a lista
        self.inicio = None
        self.proximo = None
        self.tamanho = 0
   
    def repetidos(self, elemento): # função que verifica elementos repetidos
        ponteiro = self.inicio
        quant = 0
        while(ponteiro !=None):
            if ponteiro.dado == elemento:
                quant = quant + 1
            ponteiro = ponteiro.proximo
        return quant # se houver elemento repetido, a função irá retornar um valor diferente de zero

    def __del__(self): # destroi a lista
        return 0
    
    def __getitem__(self, indice): # retorna o valor da posição
        # lista[3]
        # >>> 6
        ponteiro = self._getno(indice)
        if ponteiro:
            return ponteiro.dado
        raise IndexError("Indice fora da lista")

    def __setitem__(self, indice, elemento): # função que sobreescreve o valor na posição
        # lista[3] = 9
        # 9 sobreescreve o valor 6
        ponteiro = self._getno(indice)
        if ponteiro:
            ponteiro.dado = elemento
        else:
            raise IndexError("Indice fora da lista")

    def __len__(self): #retorna o tamanho da lista
        return self.tamanho

    def __repr__(self): # função para representar a lista
        if self.tamanho > 0:
            representacao = ""
            ponteiro = self.inicio
            while(ponteiro):
                representacao = representacao + str(ponteiro.dado) + "->"
                ponteiro = ponteiro.proximo
            return representacao
        return "Lista vazia"

    def __str__(self):
        return self.__repr__()
