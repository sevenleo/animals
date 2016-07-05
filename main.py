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


##leo ricardo teste

#test = "../data/shelter_animal/test.csv"
#train = "../data/shelter_animal/train.csv"
train = "microtrain.csv"




data = PrepareData(train)


for line in data.x:
	print(line)
	#tirar parenteses
	#animal.csv


#geracao = Generate(data.x,data.y)
geracao = Generate()
geracao.train("animal.csv")
geracao.predict("test.csv")

