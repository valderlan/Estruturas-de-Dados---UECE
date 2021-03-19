# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# Árvore AVL implementada em Pyhton 3
# Criaçao da classe Nó para uma árvore binária
class No: 
    def __init__(self, dado): 
        self.dado = dado 
        self.filho_esq = None
        self.filho_dir = None
        self.altura = 1
    def __str__(self):
        return str(self.dado)
  
# Classe de uma Árvore AVL
class ArvoreBinAVL:
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
        # Aqui é a implementação que diferencia de uma árvore binária de um AVL  
        # Calculado o fator de balanceamento para decidir se deve ou não 
        # fazer a rotação e escolher qual rotação
        balanco = self._Balanceamento(no)
        # Os quatro casos para rotação 
        # Primeiro caso: rotação simples a direita LL 
        if balanco > 1 and elemento < no.filho_esq.dado: 
            return self._Rotacao_D(no) 
        # Segundo caso: rotação simples a esquerda RR 
        if balanco < -1 and elemento > no.filho_dir.dado: 
            return self._Rotacao_E(no) 
        # Terceiro caso: rotação dupla a direita LR 
        if balanco > 1 and elemento > no.filho_esq.dado: 
            no.filho_esq = self._Rotacao_E(no.filho_esq) 
            return self._Rotacao_D(no) 
        # Quarto caso: rotação dupla a esquerda RL 
        if balanco < -1 and elemento < no.filho_dir.dado: 
            no.filho_dir = self._Rotacao_D(no.filho_dir) 
            return self._Rotacao_E(no)
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
        if no is None: 
            return no
        # Atualização da altura da árvore 
        no.altura = 1 + max(self.obterAltura(no.filho_esq), self.obterAltura(no.filho_dir))
        # Aqui é a implementação que diferencia de uma árvore binária de um AVL  
        # Calculado o fator de balanceamento para decidir se deve ou não 
        # fazer a rotação e escolher qual rotação 
        balanco = self._Balanceamento(no)
        # Os quatro casos para rotação 
        # Primeiro caso: rotação simples a direita LL 
        if balanco > 1 and self._Balanceamento(no.filho_esq) >= 0:
            return self._Rotacao_D(no) 
        # Segundo caso: rotação simples a esquerda RR 
        if balanco < -1 and self._Balanceamento(no.filho_dir) <= 0:
            return self._Rotacao_E(no)
        # Terceiro caso: rotação dupla a direita LR 
        if balanco > 1 and self._Balanceamento(no.filho_esq) < 0: 
            no.filho_esq= self._Rotacao_E(no.filho_esq)
            return self._Rotacao_D(no)
        # Quarto caso: rotação dupla a esquerda RL
        if balanco < -1 and self._Balanceamento(no.filho_dir) > 0: 
            no.filho_dir = self._Rotacao_D(no.filho_dir)
            #print('teste 6', no) 
            return self._Rotacao_E(no)
        return no 
    # Funções para realizar as rotações
    def _Rotacao_E(self, no): # Rotação RR
        no_aux = no.filho_dir 
        no.filho_dir = no_aux.filho_esq 
        no_aux.filho_esq = no 
        # atualização das alturas 
        no.altura = 1 + max(self.obterAltura(no.filho_esq), self.obterAltura(no.filho_dir)) 
        no_aux.altura = 1 + max(self.obterAltura(no_aux.filho_esq), self.obterAltura(no_aux.filho_dir)) 
        # Retorna com a nova raiz
        return no_aux
    def _Rotacao_D(self, no): # Rotação LL
        no_aux = no.filho_esq 
        no.filho_esq= no_aux.filho_dir 
        no_aux.filho_dir = no 
        # atualização das alturas
        no.altura = 1 + max(self.obterAltura(no.filho_esq), self.obterAltura(no.filho_dir)) 
        no_aux.altura = 1 + max(self.obterAltura(no_aux.filho_esq), self.obterAltura(no_aux.filho_dir)) 
        # Retorna com a nova raiz
        return no_aux 
    # --------------------------------------------------------------------
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
