#coding: utf-8

import csv
import os
import numpy as np
import json

import random, copy

from PrepareData import PrepareData
from generate import Generate


#========================= MAIN.EXEC =========================#


##leo ricardo teste

#test = "../data/shelter_animal/test.csv"
#train = "../data/shelter_animal/train.csv"
train = "microtrain.csv"




data = PrepareData(train)


for line in data.x:
	#print( line.split("[")[1].split("]")[1] )
	a=line
	#tirar parenteses
	#animal.csv
print("")

#geracao = Generate(data.x,data.y)
geracao = Generate()
geracao.train("animal_train.csv")
geracao.predict("animal_test.csv")

