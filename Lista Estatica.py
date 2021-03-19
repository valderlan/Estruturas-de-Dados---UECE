# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# estrutura para uma lista estatica sequencial
class ListaEst:
    def __init__(self, maximo):
        self.lista = [None] * maximo # define o tamanho máximo na lista dado pelo usuário
        self.max = maximo # parâmetro definido pelo o usário para o tamanho da lista
        self.tamanho = 0 # guarda o tamanho da lista
        
    def addF(self,elemento): # adiciona um elemento no final da lista
        if self.tamanho == self.max: # se lista cheia retorna a mensagem de erro
            raise IndexError("A lista está cheia")
        else:
            self.lista[self.tamanho] = elemento # add o elemento no final da lista
        self.tamanho = self.tamanho + 1
    
    def addI(self, elemento): # adiciona um elemento no inicio da lista
        if self.tamanho == self.max:
            raise IndexError("A lista está cheia")
        else:
            for i in range(self.tamanho, 0, -1):
                self.lista[i] = self.lista[i-1] # faz os ajustes para deslocar os indices dos demais elementos 
                self.lista[i-1] = self.lista[i]
            self.lista[0] = elemento # adiciona no inicio da lista
        self.tamanho = self.tamanho + 1

    def inserir(self, indice, elemento): # insere um elemento na posição desejada
        if self.tamanho == self.max:
            raise IndexError("A lista está cheia")
        if indice == 0: # se for em zero, chama a função que adiciona no inicio
            self.addI(elemento)
        elif indice == self.tamanho: # se for no final, chama a função que adiciona no final
            self.addF(elemento)
        else:
            for i in range(self.tamanho, indice, -1): 
                self.lista[i] = self.lista[i-1]
                self.lista[i-1] = self.lista[i]
            self.lista[indice] = elemento
            self.tamanho = self.tamanho + 1

    def delF(self): # deleta o ultimo elemento da lista
        if self.tamanho == 0: # se tamanho for zero, retorna uma mensagem de erro
            raise IndexError("A lista está vazia")
        else:
            self.lista[self.tamanho - 1] = None
        self.tamanho = self.tamanho - 1
        
    def delI(self): # deleta o primeiro elemento da lista
        if self.tamanho == 0:
            raise IndexError("A lista está vazia")
        else:
            self.lista[0] = None
            for i in range(0, self.tamanho - 1, 1):
                self.lista[i] = self.lista[i+1]
                self.lista[i+1] = self.lista[i]
        self.tamanho = self.tamanho - 1
    
    def indice(self, elemento): # retorna o indice do elemento procurado
        for indice in range(self.tamanho):
            if self.lista[indice] == elemento:
                return indice # encontrando o elemento, retorna o indice
            
        raise ValueError("{} não tá na lista".format(elemento))
    
    def delete(self,elemento): # deleta a primeira ocorrencia de um elemento na lista
        if self.tamanho == 0:
            raise IndexError("A lista está vazia")
        indice = self.indice(elemento)
        self.lista[indice] = None
        for i in range(indice, self.tamanho - 1, 1):
            self.lista[i] = self.lista[i+1]
            self.lista[i+1] = self.lista[i]
        self.tamanho = self.tamanho - 1

    def delind(self, indice): # deleta o elemento do indice escolhido
        if self.tamanho == 0:
            raise IndexError("A lista está vazia")
        if ((indice >= self.tamanho) or (indice < 0)):
            raise IndexError("Indice fora da lista")
        #elemento = self.lista[indice]
        self.lista[indice] = None
        for i in range(indice, self.tamanho - 1, 1):
            self.lista[i] = self.lista[i+1]
            self.lista[i+1] = self.lista[i]
        self.tamanho = self.tamanho - 1

    def limpar(self): # função para limpar toda a lista, onde os valores serão sobreescritos por None como no estado inicial
        for i in range(self.tamanho):
            self.lista[i] = None
        self.tamanho = 0 # reseta a quantidade de elementos
    
    def repetidos(self, elemento): # função que verifica elementos repetidos
        quant = 0
        for i in range(self.tamanho):
            if self.lista[i] == elemento:
                quant = quant + 1
        return quant # se houver elemento repetido, a função irá retornar um valor diferente de zero
    
    def vazia(self): # verifica se a lista está vázia
        if self.tamanho == 0:
            return True
        return False
   
    def __del__(self): # função que exluir toda a lista
        # del lista
        return 0

    def __getitem__(self, indice): # retorna o valor da posição
        # lista[3]
        # >>> 6
        if ((indice >= self.tamanho) or (indice < 0)):
            raise IndexError("Indice fora da lista")
        else:
            return self.lista[indice]

    def __setitem__(self, indice, elemento): # função que sobreescreve o valor na posição
        # lista[3] = 9
        # 9 sobreescreve o valor 6
        if ((indice >= self.tamanho) or (indice < 0)):
            raise IndexError("Indice fora da lista")
        else:
            self.lista[indice] = elemento

    def __len__(self): # retorna com o tamanho da lista
        # len(lista)
        return self.tamanho
    
    def __repr__(self): # função para representar a lista
        if self.tamanho > 0:
            representacao = "["
            for i in range(0, self.tamanho):
                if i != self.tamanho -1:
                    ponteiro = self.lista[i]
                    representacao = representacao + str(ponteiro) + ", "
                else:
                    ponteiro = self.lista[i]
                    representacao = representacao + str(ponteiro)
            representacao = representacao + "]"      
            return representacao
        return "Lista Vazia"

    def __str__(self):
        return self.__repr__()
