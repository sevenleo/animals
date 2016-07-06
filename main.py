#coding: utf-8

import csv
import os
import numpy as np
import json

import random, copy

from PrepareData import PrepareData
from generate import Generate


#========================= MAIN.EXEC =========================#


#test = "../data/shelter_animal/test.csv"
#train = "../data/shelter_animal/train.csv"
train = "train.csv"


data = PrepareData(train)


f = open('animal_train.csv', 'wb')
for line in data.x:
	f.write((str(line)).split("[")[1].split("]")[0] + "\n")


print("Trantando dados gerados ......................... ")

geracao = Generate(data.x,data.y)

geracao.predict_class(data.x,data.y,"animal_test.csv")
