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



#test = "../data/shelter_animal/test.csv"
#train = "../data/shelter_animal/train.csv"
train = "microtrain.csv"




data = PrepareData(train)


#for line in data.x:
	#print(line)
	#tirar parenteses
	#animal.csv


#Generate(data.x,data.y)
Generate.train("animal.csv")

