#coding: utf-8

import csv
import os
import numpy as np

import random, copy

#os.system('cls')
# 0
# AnimalID   

# 1         2           3           4               5           6               7               8       9
# Name    DateTime    OutcomeType OutcomeSubtype  AnimalType SexuponOutcome  AgeuponOutcome  Breed   Color
#   3       x           5           16              2           2   + 3            9999         2       2


#-------------------------PrepareData 
class PrepareData:
    X  = [] #numpy
    x  = [] #matrix normal = array2D
    y  = [] #array de saida = valor esperado
    y2 = [] #dados adicionais
    def __init__(self,file):
        
        # self.x.append("zero")
        #self.x.extend(["AnimalID","Name","DateTime","AnimalType","SexuponOutcome","AgeuponOutcome","Breed","Color"])
        #print( self.x[0:8])

        with open(file, 'r') as csv_file:
            train = csv.reader(csv_file, delimiter=',')
            end=0
            for i, row in enumerate(train):
                if i != 0: 

                    self.y.append ( self.OutcomeType(row[3]) )
                    self.y2.append ( self.OutcomeSubtype(row[4]) )

                    
                    #criar o numpy part 1/2
                    '''
                    #print ( "\n")
                    self.x.extend ( [row[0]]) ##remover
                    self.x.extend ( [self.Name(row[1])])
                    self.x.extend ( [self.AnimalType(row[5])])
                    self.x.extend ( [self.SexuponOutcome1(row[6])] )
                    self.x.extend ( [self.SexuponOutcome2(row[6]) ])
                    self.x.extend ( [self.AgeuponOutcome(row[7])] )
                    self.x.extend ( [self.Breed(row[8]) ])
                    self.x.extend ( [self.Color1(row[9])] )
                    self.x.extend ( [self.Color2(row[9]) ] )
                    '''

                    #criar matrix comum = array de 2 dimensoes
                    self.x.append( [self.Name(row[1]) , self.AnimalType(row[5]) , self.SexuponOutcome1(row[6]) , self.SexuponOutcome2(row[6]) , self.AgeuponOutcome(row[7]) , self.Breed(row[8])  , self.Color1(row[9]) , self.Color2(row[9]) ])
 
               #endif
            #endfor 
        #endwith
        
        #self.X=np.array(x).reshape(len(x)/9,9) #criar o numpy part 2/2
        #self.Printer(len(x)/9) #printar o numpy part

    #end__init__

    def Printer(self,lines):
        for i in xrange(lines):
            print(self.X[i]) #matrix
            print(self.y[i]) #retorno_esperado #OutcomeType
            print(self.y2[i]) #retorno_esperado2 #OutcomeSubType
            print("\n")


    #SWITCHS
    #http://www.pydanny.com/why-doesnt-python-have-switch-case.html
    def Name(self,value):
        if value is '':
            return 1
        else:
            return 2

    def OutcomeType(self, value):
        options = {
            'Return_to_owner': 1,
            'Euthanasia': 2,
            'Adoption': 3,
            'Transfer': 4,
            'Died': 5
        }

        return options.get(value,-1)


    def OutcomeSubtype(self, value):
        options = {
            'Foster': 1,
            'In Foster': 1,
            'Partner': 2,
            'Offsite': 3,
            'SCRP': 4,
            'Aggressive': 5,
            'Behavior': 6,
            'Medical': 7,
            'Rabies Risk': 8,
            'In Kennel': 9,
            'Enroute': 10,
            'At Vet': 11,
            'In Surgery': 12,
            'Barn': 13,
            'Court/Investigation': 14,
            'Suffering': 15,
            '': 16
        }
        #print ( value)
        return options.get(value,-1)


    def AnimalType(self, value):
        options = {
            'Dog': 1,
            'Cat': 2
        }
        #print ( value)
        return options.get(value,-1)


    def SexuponOutcome1(self, value):
        options = {
            'Intact': 1,
            'Spayed': 2,
            'Neutered': 3,
            'Unknown': 4
        }
        
        #print ( value.split(" ")[0] )
        return options.get(value.split(" ")[0],-1)


    def SexuponOutcome2(self, value):

        if value.endswith("Male"):
            #print ( "Male" )
            return 1
        else:
            #print ( "Female" )
            return 2


    def AgeuponOutcome(self, value):
        
        if value is '': 
            return -1
        else:
            number = value.split(" ")[0]
            string = value.split(" ")[-1]

            if string.startswith("year"):
                number=int(number)*365
            elif string.startswith("month"):
                number=int(number)*30
            elif string.startswith("weeks"):
                number=int(number)*7
            
            #print ( number )
            return number
       

    def Breed (self, value):
        if value.endswith("Mix"):
            #print ( "Mix" )
            return 2
        else:
            #print ( "Pure" )
            return 1


    def Color1 (self, value):
        #print ( value.split("/")[0] )
        #return value.split("/")[0]
        options = {
            'Black': 10,
            'Blue': 1,
            'Brown': 2,
            'Gray': 3,
            'Orange': 4,
            'Red': 5,
            'Sable': 6,
            'Tan': 7,
            'Tricolor': 8,
            'White': 9 
        }
        return options.get( value.split(" ")[0], -1)


    def Color2 (self, value):
        #print ( value.split("/")[1:] )
        #color2 = value.split("/")[1:] //como tratar se nao existe?
        #color1,color2 = value.split("/") //como tratar se nao existe?
        #solucao1:

        if value.split("/")[0] == value.split("/")[-1]:
            return 1
        else:
            #return value.split("/")[-1]
            return 2


#-------------------------Perceptron
class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):

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
    def testar(self, amostra, classe1, classe2):

        # insere o -1
        amostra.insert(0, -1)
        

        '''
            utiliza-se o vetor de pesos ajustado
            durante o treinamento da rede
        '''
        u = 0
        for i in range(self.num_amostra + 1):
            u += self.pesos[i] * float(amostra[i])
        print(u)

        # calcula a saída da rede
        y = self.sinal(u)

        # verifica a qual classe pertence
        #if y == -1:
        #    print('A amostra pertence a classe %s' % classe1)
        #else:
        #    print('A amostra pertence a classe %s' % classe2)


    def degrau(self, u):
        return 1 if u >= 0 else 0


    def sinal(self, u): # é a mesma função degrau bipolar
        return 1 if u >= 0 else -1


#-------------------------Perceptron2
class Perceptron2:
        x = []
        y = []
        def __init__(self,_x,_y):
                self.x = _x
                self.y = _y
                '''
                with open("./perceptron/dataset.csv", 'r') as csv_file:
                        csv_file = csv.reader(csv_file, delimiter=';')

                        for row in csv_file:
                                xi = []
                                xi.append(float(row[0]))
                                xi.append(float(row[1]))
                                xi.append(float(row[2]))
                                self.y.append(row[3])
                                self.x.append(xi)
				'''
                self.fit()

        def fit(self):

                #self.W=np.ones(len(self.x[0])) 
                self.W=np.ones(8) #teste
                self.B=1
                
                delta = 10^5
                erro_i = 10^5
                self.l_rate = 0.8
                self.margem_de_erro = 0.05

                n = 0
                while delta > self.margem_de_erro:
                        i = 0
                        ErroTotal = 0
                        while i < len(self.x):
                                self.x[i] = np.array(self.x[i])

                                Y = 1/(1 + np.e ** - np.dot(self.W, self.x[i]) + self.B)

                                erro = np.float64(self.y[i]) - Y

                                ErroTotal = ErroTotal + abs(erro)
                                self.learn_erro(self.x[i], erro)
                                #print("----------------------------------------")
                                #print(self.W)
                                i = i + 1
                        delta = abs(erro_i - ErroTotal)
                        erro_i = ErroTotal
                        n = 1 + n

        def learn_erro(self, xi, erro):
                self.W = self.W + self.l_rate * erro * xi
                self.B = self.B + self.l_rate * erro

        def predict(self, X):
                saida = []
                for xi in X:
                        if np.dot(self.W, xi) < 0.5:
                                saida.append(0)
                        else:
                                saida.append(1)

                return saida


#========================= MAIN.EXEC =========================#



microtrain =  "microtrain.csv"   
train = "../data/shelter_animal/train.csv"
train = "train.csv"
test = "../data/shelter_animal/test.csv"
data = PrepareData(train)

#print(data.x)
#print( np.array(data.y) )
#print(data.y2)



#-------------------------Perceptron
print("iniciando:")
testes = copy.deepcopy(data.x)

print("treinando:")
rede = Perceptron(amostras=data.x, saidas=data.y, taxa_aprendizado=0.5, epocas=1000)
rede.treinar()

print("testando:")
for teste in testes:
    rede.testar(teste, 'A', 'B')
    #rede.testar(teste, 'Return_to_owner', 'Euthanasia', 'Adoption', 'Transfer', 'Died')


'''

         
#-------------------------Perceptron2

treinox = np.array(data.x).astype(int)
treinoy = np.array(data.y).astype(int)

rede = Perceptron2(treinox,treinoy)

testes = np.array(data.x).astype(int)

print(rede.predict(testes))
'''


#=========================comentarios=========================#
"""
	Separar as raças populares para adocao.

	Raças disponiveis (sem mixes):
	Airedale Terrier
	Akita
	American Bulldog
	American Pit Bull Terrier
	American Staffordshire Terrier
	Anatol Shepherd
	Angora
	Australian Cattle Dog
	Australian Shepherd
	Basset Hound
	Beagle
	Bernese Mountain Dog
	Black
	Black Mouth Cur
	Blue Lacy
	Border Collie
	Border Terrier
	Boxer
	Breed
	Cairn Terrier
	Cardigan Welsh Corgi
	Catahoula
	Chesa Bay Retr
	Chihuahua Longhair
	Chihuahua Shorthair
	Chinese Sharpei
	Chow Chow
	Cocker Spaniel
	Collie Smooth
	Dachshund
	Dachshund Longhair
	Dachshund Wirehair
	Doberman Pinsch
	Dogo Argentino
	Dogue De Bordeaux
	Domestic Longhair
	Domestic Medium Hair
	Domestic Shorthair
	English Bulldog
	English Foxhound
	English Pointer
	Exotic Shorthair
	Flat Coat Retriever
	German Shepherd
	Great Dane
	Great Pyrenees
	Italian Greyhound
	Jack Russell Terrier
	Labrador Retriever
	Lhasa Apso
	Maltese
	Manchester Terrier
	Manx
	Miniature Pinscher
	Miniature Poodle
	Miniature Schnauzer
	Norfolk Terrier
	Pit Bull
	Plott Hound
	Pointer
	Queensland Heeler
	Rat Terrier
	Rhod Ridgeback
	Rottweiler
	Russian Blue
	Scottish Terrier
	Shetland Sheepdog
	Shih Tzu
	Siamese
	Siberian Husky
	Tan Hound
	Tibetan Terrier
	Treeing Walker Coonhound
	Vizsla
	Whippet
	Yorkshire Terrier
	Yorkshire Terrier 
"""

