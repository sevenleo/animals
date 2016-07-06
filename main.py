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

#for line in data.x:
	#tirar parenteses
	#animal.csv
	#print( line.split("[")[1].split("]")[1] )
	#print(line)

print("Trantando dados gerados ......................... ")
geracao = Generate(data.x,data.y)


#geracao.train("animal_train.csv")
geracao.predict_class(data.x,data.y,"animal_test.csv")
