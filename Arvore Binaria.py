# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# Árvore Binária implementada em Pyhton 3
# Composta de alguns metodos para operar em uma arvore binaria de busca
# Criaçao da classe Nó para uma árvore binária
class No: 
    def __init__(self, dado): 
        self.dado = dado 
        self.filho_esq = None
        self.filho_dir = None
        self.altura = 1
    def __str__(self):
        return str(self.dado)
# Classe de uma Árvore Binária 
class ArvoreBin:
    def __init__(self):
        self.raiz = None 
    # Função para inserir elemento na árvore
    # O usuário não precisa informar a raíz, apenas informar os elementos
    # para inserir na árvore 
    def inserir(self, elemento):
        self.raiz = self._inserir(elemento, self.raiz)
        return self.raiz
    # Função chamada pela função inserir que passar o dado raiz   
    def _inserir(self, elemento, no):
        if no is None: # Condição de retorno da recursividade
            no = No(elemento)
            return no 
        elif elemento < no.dado: # Se elemento menor que raiz, ficará a esquerda
            no.filho_esq = self._inserir(elemento, no.filho_esq) 
        else: # Se elemento maior que raiz, ficará a direita
            no.filho_dir = self._inserir(elemento, no.filho_dir) 
        # Atualização da altura da árvore
        no.altura = 1 + max(self.obterAltura(no.filho_esq), self.obterAltura(no.filho_dir))
        return no

    # Função para remover elemento na árvore
    def remover(self,elemento):
        if  self.raiz is None:
                return print('Árvore vazia')
        self.raiz = self._remover(elemento, self.raiz)
    def _remover(self, elemento, no):
        if no is None: # Condição de retorno da recursividade
            return no
        elif elemento < no.dado: 
            no.filho_esq = self._remover(elemento, no.filho_esq)
        elif elemento > no.dado: 
            no.filho_dir = self._remover(elemento, no.filho_dir)
        # entrará o Else, após localizar o elemento na árvore
        else: # Casos que o elemento não tem filhos ou apenas um filho
            if no.filho_esq is None: 
                no = no.filho_dir 
                return no 
            elif no.filho_dir is None: 
                no = no.filho_esq
                return no
            # Caso onde o elemente tem dois filhos  
            temp = self.minimo(no.filho_dir) 
            no.dado = temp.dado 
            no.filho_dir = self._remover(temp.dado, no.filho_dir)
        
        # Atualização da altura da árvore        
        no.altura = 1 + max(self.obterAltura(no.filho_esq), self.obterAltura(no.filho_dir))
        return no
    # Função para calcular altura da árvore em um nó  
    def obterAltura(self, no): 
        if no is None: 
            return 0
        return no.altura
    # Função para calcular a altura da árvore
    def AlturaARV(self, no = 0): # retorna a altura de uma árvore
        if no == 0:
            no = self.raiz # seleciona a raiz para determinar a altura da árvore se ela não estiver vazia
            if no is None:  # caso não tenha raiz, isto é, árvora vazia
                return print("Árvore vazia")
        if no is None:
            return 0
        return max(self.AlturaARV(no.filho_esq),self.AlturaARV(no.filho_dir)) + 1
    # Função para verificar se árvore tá balanceada
    def _Balanceamento(self, no): 
        if no is None: 
            return 0
        return self.obterAltura(no.filho_esq) - self.obterAltura(no.filho_dir) 
    # Função para informar o menor elemento em uma árvore
    def MenorElem(self, no = None): # retorna o menor valor de uma árvore
        if no is None:
            no = self.raiz
            if no is None:  # caso não tenha raiz, isto é, árvora vazia
                return print("Árvore vazia")
        while no.filho_esq is not None:
            no = no.filho_esq
        return no.dado
    def minimo(self, no): 
        if no is None or no.filho_esq is None: 
            return no
        return self.minimo(no.filho_esq)
    # Função para informar o maior elemento em uma árvore
    def MaiorElem(self, no = None): # retorna o maior valor de uma árvore
        if no is None:
            no = self.raiz
            if no is None: # caso não tenha raiz, isto é, árvora vazia
                return print("Árvore vazia")
        while no.filho_dir is not None:
            no = no.filho_dir
        return no.dado
    def maximo(self, no):
        if no is None or no.filho_dir is None:
            return no
        return self.maximo(no.filho_dir)
    # Função que busca elemento em uma árvore
    def buscar(self, elemento):
        if self.raiz is None:
            return print("Árvore vazia")
        no_atual = self.raiz
        while no_atual.dado != elemento:
            if elemento < no_atual.dado:
                no_atual = no_atual.filho_esq
            else:
                no_atual = no_atual.filho_dir
            if no_atual is None:
                return None
        return no_atual

    def contarNo(self, no = 0): # conta o números de nós da árvore, defino valor zero
        if no == 0:             # apenas para não precisar passa parametro na chamada
           no = self.raiz
           if no is None:  # caso não tenha raiz, isto é, árvora vazia
               return print("Árvore vazia")
        if no is None:
            return 0
        else:
            return self.contarNo(no.filho_esq) + self.contarNo(no.filho_dir) + 1

    def vazia(self): # verifica se a árvora está vazia ou não
        if self.raiz:
            return False
        else:
            return True

    def balanceada(self, no = 0): # Verifica se a árvore tá balanceada
        if no == 0:
            no = self.raiz
        if no is None:
            return True
        altura_esquerda = self.AlturaARV(no.filho_esq)
        altura_direita = self.AlturaARV(no.filho_dir)
        if abs(altura_esquerda - altura_direita) > 1:
            return False
        return self.balanceada(no.filho_esq) and self.balanceada(no.filho_dir)
    # Caminhos para percorrer em uma árvore
    def pre_ordem(self, no = None): # os filhos de um nó são processados após o nó
        if self.raiz is None:
            return print("Árvore vazia")
        if no is None:
            no = self.raiz
        print(no, end = ' ')
        if no.filho_esq:
            self.pre_ordem(no.filho_esq)
        if no.filho_dir:
            self.pre_ordem(no.filho_dir)
    def em_ordem(self, no = None): # processa o filho à esquerda, o nó e o filho a direita
        if self.raiz is None:
            return print("Árvore vazia")
        if no is None:
            no = self.raiz
        if no.filho_esq:
            #print('(', end = '')
            self.em_ordem(no.filho_esq)
        print(no, end = ' ')
        if no.filho_dir:
            self.em_ordem(no.filho_dir)
            #print(')', end = '')
    def pos_ordem(self, no = None): # os filhos processados antes do nó
        if self.raiz is None:
            return print("Árvore vazia")
        if no is None:
            no = self.raiz
        if no.filho_esq:
            self.pos_ordem(no.filho_esq)
        if no.filho_dir:
            self.pos_ordem(no.filho_dir)
        print(no, end = ' ')
