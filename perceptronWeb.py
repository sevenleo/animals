#coding: utf-8
class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado, epocas, limiar=-1):
        print("PerceptronWeb ...............")
        self.amostras = amostras # todas as amostras
        self.saidas = saidas # saídas respectivas de cada amostra
        self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
        self.epocas = epocas # número de épocas
        self.limiar = limiar # limiar
        self.num_amostras = len(amostras) # quantidade de amostras
        self.num_amostra = len(amostras[0]) # quantidade de elementos por cada amostra
        self.pesos = [] # vetor dos pesos


    # função utilizada para treinar a rede
    def treinar(self):
        
        # adiciona -1 para cada amostra
        for amostra in self.amostras:
            amostra.insert(0, -1)
        
        # inicia o vetor de pesos com valores aleatórios pequenos
        for i in range(self.num_amostra):
            self.pesos.append(random.random())
        print(self.pesos)

        # insere o limiar no vetor de pesos
        self.pesos.insert(0, self.limiar)

        num_epocas = 0 # inicia o contador de épocas
        
        while True:

            erro = False # erro inicialmente inexiste

            # para todas as amostras de treinamento
            for i in range(self.num_amostras):
                
                u = 0
                '''
                    realiza o somatório, o limite (self.num_amostra + 1) 
                    é porque foi inserido o -1 em cada amostra
                '''
                for j in range(self.num_amostra + 1):
                    

                    u += self.pesos[j] * float(self.amostras[i][j])

                # obtém a saída da rede utilizando a função de ativação

                y = self.sinal(u)

                # verifica se a saída da rede é diferente da saída desejada
                if y != self.saidas[i]:

                    # calcula o erro: subtração entre a saída desejada e a saída da rede
                    erro_aux = self.saidas[i] - y

                    # faz o ajuste dos pesos para cada elemento da amostra
                    for j in range (self.num_amostra + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * float(self.amostras[i][j])

                    erro = True # se entrou, é porque o erro ainda existe
            
            num_epocas += 1 # incrementa o número de épocas

            # critério de parada é pelo número de épocas ou se não existir erro
            if num_epocas > self.epocas or not erro:
                break
        


    # função utilizada para testar a rede
    # recebe uma amostra a ser classificada e os nomes das classes
    # utiliza função sinal, se é -1 então é classe1, senão é classe2
    def testar(self, amostra, classe1, classe2, classe3, classe4, classe5):

        # insere o -1
        amostra.insert(0, -1)
        

        '''
            utiliza-se o vetor de pesos ajustado
            durante o treinamento da rede
        '''
        u = 0
        for i in range(self.num_amostra + 1):
            u += self.pesos[i] * float(amostra[i])
            

        # calcula a saída da rede
        y = self.sinal(u)
        print(u)


        # verifica a qual classe pertence
        #if y == -1:
        #    print('A amostra pertence a classe %s' % classe1 ,u)
        #else:
        #    print('A amostra pertence a classe %s' % classe2,u)


    def degrau(self, u):
        return 1 if u >= 0 else 0


    def sinal(self, u): # é a mesma função degrau bipolar
        return 1 if u >= 0 else -1

