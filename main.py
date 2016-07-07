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
test = "test.csv"

print("Deseja treinar [digite 0] ou calcular as probabilidades aleatóriamente [digite 1] ?")
treino = int( raw_input())

if treino !=1:
	print("Treino = train.csv\nTest = test.csv")
	print("Treinar por quantas epocas?")
	epocas = int( raw_input())
	print("E ciclos?")
	ciclos = int(raw_input())
	print("O Arquivo de saida estara em animal_output.csv")

print("Gerando csv detalhado (animal_train.csv) a partir do arquivo train.csv  ......................... ")
data = PrepareData(train)
f = open('animal_train.csv', 'wb')
for line in data.x:
	f.write((str(line)).split("[")[1].split("]")[0] + "\n")
f.close()

print("Gerando csv detalhado (animal_test.csv) a partir do arquivo test.csv ......................... ")
t = open('animal_test.csv', 'wb')
for line in data.PrepareTestFile(test):
	#f.write((str(line)).split("[")[1].split("]")[0] + "\n")
	t.write(str(line) + "\n")
t.close()

print("Trantando dados gerados ......................... ")
geracao = Generate(data.x,data.y)

if treino !=1:
	## TRAIN PREDICT
	geracao.predict_class(data.x,data.y,"animal_test.csv",epocas,ciclos)

if treino ==1:
	## RANDOM
	lines=0
	with open ('test.csv','rb') as f:
	    for line in f:
	        lines+=1

	print ("Linhas: ",lines-1)
	geracao.random(lines-1)