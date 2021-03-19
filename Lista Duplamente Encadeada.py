# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura que define um no
class No: 
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None # aponta para o proximo elemento 
        self.anterior = None # aponta para o elemento anterior

# estrutura que define uma lista duplamente encadeada
class ListaDEnc: # ao ser chamada uma lista vazia é criada
    def __init__(self):
        self.inicio = None # guarda o inicio da lista
        self.fim = None # guarda o final da lista
        self.tamanho = 0 # guarda o tamanho da lista
# -------------------------------------------------------------------------------------------------------
# foram criadas 3 funções para adicionar um elemento da lista duplamente encadeada
# uma para adicionar no começo addI, uma para adicionar no final addF
# e uma chamada inserir, onde posso alocar em qq lugar da lista

    def addF(self, elemento): # add um elemento no final
        no = No(elemento)
        if self.inicio: # insere elemento no final da lista quando já tem um elemento
            self.fim.proximo = no
            no.anterior = self.fim
            no.proximo = None
            self.fim = no
        else: # insere o primeiro elemento na lista
            self.inicio = no
            self.fim = no #
        self.tamanho = self.tamanho + 1
    
    def addI(self,elemento): # add um elemento no inicio
        no = No(elemento)
        if self.inicio: # insere elemento no inicio da lista quando já tem um elemento
            no.proximo = self.inicio
            self.inicio.anterior = no
            no.anterior = None
            self.inicio = no
        else: # insere o primeiro elemento na lista
            self.inicio = no
            self.fim = no
        self.tamanho = self.tamanho + 1

    def _getno(self, indice): # informa o no
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
            no.proximo = ponteiro.proximo #guarda a ligação que estava
            ponteiro.proximo.anterior = no
            ponteiro.proximo = no
            no.anterior = ponteiro
            self.tamanho = self.tamanho + 1
# -------------------------------------------------------------------------------------------------------
# ao exemplo do adicionar elementos na lista duplamente encadeada, aqui foram criadas tambem
# 3 funções para eliminar um elemento na lista. Eliminar no inicio da lista delI
# eliminar o elemento no final da lista delF e eliminar o elemento em sua primeira ocorrência
# função delete onde se passa o elemento que desejamos eliminar 
    def delI(self): # deleta o primeiro elemento
        if self.vazia():
            raise IndexError("A lista está vazia")
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        self.tamanho = self.tamanho - 1

    def delF(self): # deleta o ultimo elemtno
        if self.vazia():
            raise IndexError("A lista está vazia")
        elif self.tamanho == 1:
            #elemento = self.fim.dado
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        self.tamanho = self.tamanho - 1

    def indice(self, elemento): # informa o indice do elemento
        ponteiro = self.inicio
        indiceElemento=0
        while(ponteiro):
            if ponteiro.dado == elemento:
                return indiceElemento
            ponteiro = ponteiro.proximo
            indiceElemento = indiceElemento + 1
        raise ValueError("{} não tá na lista".format(elemento))

    def delete(self,elemento): #deleta a primeira ocorrencia de um elemento
        if self.inicio == None:
            raise ValueError("{} não tá na lista".format(elemento))
        elif self.inicio.dado == elemento:
            self.delI()
            return True
        elif self.fim.dado == elemento:
            self.delF()
            return True
        else:
            antr = self.inicio
            ponteiro = self.inicio.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    antr.proximo = ponteiro.proximo
                    ponteiro.proximo.anterior = antr 
                    ponteiro.proximo = None
                antr = ponteiro
                ponteiro = ponteiro.proximo
            self.tamanho = self.tamanho - 1
            return True
        raise ValueError("{} não tá na lista".format(elemento))
# -------------------------------------------------------------------------------------------------------    
    def inverter(self): # inverte o sintido de uma lista
        li_invt = ListaDEnc()
        ponteiro = self.fim
        while(ponteiro):
            li_invt.addF(ponteiro.dado)
            ponteiro = ponteiro.anterior
        return li_invt

    def vazia(self): # infroma se a lista tá vazia 
        if self.tamanho == 0:
            return True
        return False

    def limpar(self): # função para limpar toda a lista
        self.inicio = None
        self.fim = None
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
    
    def __del__(self): # remove toda a lista
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
        # len(lista)
        return self.tamanho

    def __repr__(self): # função para representar a lista
        if self.tamanho > 0:
            representacao = "<-"
            ponteiro = self.inicio
            r = 0
            while(ponteiro):
                if r == 0:
                    representacao = representacao + str(ponteiro.dado)
                if (ponteiro != None) and (r != 0):
                    representacao = representacao + "<->" + str(ponteiro.dado)
                ponteiro = ponteiro.proximo
                if ponteiro is None:
                    representacao = representacao + "->"
                    break
                r = 1
            return representacao
        return "Lista vazia"

    def __str__(self):
        return self.__repr__()
