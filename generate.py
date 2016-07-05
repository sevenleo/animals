#coding: utf-8
import csv
import os
import numpy as np
import random, copy
import cPickle as pickle
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

class Generate:
       
        def __init__(self,_x,_y):
                print("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer")



        def random(self):
                X=_x
                y=_y
                i=1
                for line in X:
                        print( "{},{},{},{},{},{}".format(i,random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),) )
                        i=i+1                

        def train(self,train_file):
                "train a regression MLP"

                #arquivo onde serao gravados os dados de treino
                output_model_file = 'model.pkl'

                ## ???        
                hidden_size = 100 ## precisaremos mudar?
                
                ##quantidade de epocas
                epochs = 6 

                # carrega o arquivo de treino
                train = np.loadtxt( train_file, delimiter = ',' )

                #separa em pares 
                x_train = train[:,0:-1]   #par = (tudo , tudo-ultimo)
                y_train = train[:,-1]     #par = (tudo , ultimo)

                #transpoe linhas em colunas
                y_train = y_train.reshape( -1, 1 )

                #calcula o tamanho do arrays
                input_size = x_train.shape[1]
                target_size = y_train.shape[1]


                # prepara o  dataset
                ds = SDS( input_size, target_size ) #cria o data set com o tamanho da matriz lida
                ds.setField( 'input', x_train ) #seta o tamanho dos campos
                ds.setField( 'target', y_train ) #seta o tamanho dos campos


                #inicia o treino
                net = buildNetwork( input_size, hidden_size, target_size, bias = True )
                trainer = BackpropTrainer( net, ds )

                print ("training for {} epochs...".format( epochs ))

                for i in range( epochs ):
                        mse = trainer.train()
                        rmse = sqrt( mse )
                        print ( "training RMSE, epoch {}: {}".format( i + 1, rmse ) )
                        
                #gera arquivo de saida       
                pickle.dump( net, open( output_model_file, 'wb' ))
