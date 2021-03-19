# em python 3 - disciplina Estrutura de Dados 1 - UECE 2020.1
# Tabela Hash com enderecamento aberto e hashing linear para resolver colisoes
# Classe de uma tabela hash
class TabelaHash: 
    def __init__(self):
        self.tamanhoT = 107
        self.slots = [None] * self.tamanhoT
        self.dado = [None] * self.tamanhoT
    # método que será calculada a posição pela divisão da chave pelo tamanho da tabela
    def funsaohash(self, chave, tamanho):
        return chave%tamanho
    # método que sejá usado quando houver colisão. Linear e será recoloado 3 posicoes seguintes
    # o numeral três foi escolhido para evitar aglomeracao em torno de uma posicao 
    def rehash(self, antigo, tamanho):
        return (antigo + 3)%tamanho
    # método para inserir um elemento na tabela hash
    def colocar(self, chave, dado):
        tamanho = len(self.slots)
        valorhash = self.funsaohash(chave, tamanho) # calculo da posição
        if self.slots[valorhash] == None: # se disponivel é inserido 
            self.slots[valorhash] = chave
            self.dado[valorhash] = dado 
        else: # se não é tratado a colisão 
            if self.slots[valorhash] == chave:
                self.dado[valorhash] = dado
            else:
                proximo_slot = self.rehash(valorhash, tamanho)
                # Faz a busca até encontrar uma posição vazia para inserir a chave e o dado relacionado a ela
                while self.slots[proximo_slot] != None and self.slots[proximo_slot] != chave:
                    proximo_slot = self.rehash(proximo_slot, tamanho)
                if self.slots[proximo_slot] == None:
                    self.slots[proximo_slot] = chave
                    self.dado[proximo_slot] = dado
                else:
                    self.dado[proximo_slot] = dado
    # método de busca do dado referente a uma chave
    def obter(self, chave):
        tamanho = len(self.slots)
        valorhash = self.funsaohash(chave, tamanho) # calculo da posição
        dado = None
        parar = False
        encontado = False
        posicao = valorhash
        # busca pelos dados referente a chave solicitada
        while self.slots[posicao] != None and not encontado and not parar:
            if self.slots[posicao] == chave:
                encontado = True
                dado = self.dado[posicao]
            else:# se não estiver na posicao calculada, irá recalcular a posição
                posicao = self.rehash(posicao, tamanho)
                if posicao == valorhash:
                    parar = True
        return dado

    def __getitem__(self, chave):
        return self.obter(chave)

    def __setitem__(self, chave, dado):
        self.colocar(chave, dado)

# teste onde se deve ser lido uma linha com duas colunas
# a primeira coluna a chave e na segunda o nome
if __name__ == "__main__":
    
    agendaT = TabelaHash()
    for i in range(10):
        entrada = input().split()
        agendaT.colocar(int(entrada[0]),entrada[1]) # chama a função colocar onde se passa a chave e os dados
    N = int(input())
    for i in range(N):
        nomes = (int(input()))
        print(agendaT[nomes])
