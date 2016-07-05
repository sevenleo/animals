#coding: utf-8

import csv
import os
import numpy as np
import json

import random, copy

from PrepareData import PrepareData
from perceptronWeb import Perceptron
from perceptronLeo import Perceptron2
from generate import Generate


#========================= MAIN.EXEC =========================#



microtrain =  "microtrain.csv"
train = "../data/shelter_animal/train.csv"
train = "train.csv"
test = "../data/shelter_animal/test.csv"



data = PrepareData(microtrain)


for line in data.x:
	print(line)
#Generate(data.x,data.y)


#-------------------------Perceptron
'''
testes = copy.deepcopy(data.x)

rede = Perceptron(amostras=data.x, saidas=data.y, taxa_aprendizado=0.5, epocas=1000)
rede.treinar()
print(rede.pesos)
for teste in testes:
    rede.testar(teste, 'Return_to_owner', 'Euthanasia', 'Adoption', 'Transfer', 'Died')

'''



#-------------------------Perceptron2

'''
treinox = np.array(data.x).astype(int)
treinoy = np.array(data.y).astype(int)

rede = Perceptron2(treinox,treinoy)

testes = np.array(data.x).astype(int)

print(rede.W) #pesos
#print(rede.predict(testes))

'''
