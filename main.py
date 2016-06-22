#coding: utf-8


from PrepareData import PrepareData
from perceptronWeb import Perceptron
from perceptronLeo import Perceptron2


#========================= MAIN.EXEC =========================#



microtrain =  "microtrain.csv"   
train = "../data/shelter_animal/train.csv"
train = "train.csv"
test = "../data/shelter_animal/test.csv"


data = PrepareData(microtrain)




#-------------------------Perceptron

'''
print('\nA ou B?\n')

# todas as amostras (total de 4 amostras)
amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], 
			[0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]

# saídas desejadas de cada amostra
saidas = [1, -1, -1, 1]

# conjunto de amostras de testes
testes = copy.deepcopy(amostras)

# cria uma rede Perceptron
rede = Perceptron(amostras=amostras, saidas=saidas, 
					taxa_aprendizado=0.1, epocas=1000)

# treina a rede
rede.treinar()

for teste in testes:
	rede.testar(teste, 'A', 'B','c','d','e')

'''
'''
#print("iniciando:")
testes = copy.deepcopy(data.x)

#print("treinando:")
rede = Perceptron(amostras=data.x, saidas=data.y, taxa_aprendizado=0.5, epocas=1000)
rede.treinar()

#print("testando:")
for teste in testes:
    rede.testar(teste, 'Return_to_owner', 'Euthanasia', 'Adoption', 'Transfer', 'Died')
'''



         
#-------------------------Perceptron2

'''
treinox = np.array(data.x).astype(int)
treinoy = np.array(data.y).astype(int)

rede = Perceptron2(treinox,treinoy)

testes = np.array(data.x).astype(int)

print(rede.predict(testes))
'''

