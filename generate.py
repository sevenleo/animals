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
from sklearn.metrics import mean_squared_error as MSE

class Generate:
       
        #def __init__(self,_x,_y):
        def __init__(self):
                print("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer")


        '''
        def random(self):
                X=_x
                y=_y
                i=1
                for line in X:
                        print( "{},{},{},{},{},{}".format(i,random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),) )
                        i=i+1                
        '''

        def train(self,train_file):
                "train a regression MLP"

                #arquivo onde serao gravados os dados de treino
                output_model_file = 'model.pkl'

                ## ???        
                hidden_size = 100 ## precisaremos mudar?
                
                ##quantidade de epocas
                epochs = 6 

                # carrega o arquivo de treino
                print( "...")
                train = np.loadtxt( train_file, delimiter = ',' )
                print( ".................")
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

        def predict(self,test_file):
                model_file = 'model.pkl'
                output_predictions_file = 'saida_predictions.txt'

                # load model
                net = pickle.load( open( model_file, 'rb' ))

                # load data
                test = np.loadtxt( test_file, delimiter = ',' )
                x_test = test[:,0:-1]
                y_test = test[:,-1]
                y_test = y_test.reshape( -1, 1 )

                # you'll need labels. In case you don't have them...
                y_test_dummy = np.zeros( y_test.shape )

                input_size = x_test.shape[1]
                target_size = y_test.shape[1]

                assert( net.indim == input_size )
                assert( net.outdim == target_size )

                # prepare dataset
                ds = SDS( input_size, target_size )
                ds.setField( 'input', x_test )
                ds.setField( 'target', y_test_dummy )

                # predict

                p = net.activateOnDataset( ds )
                        
                mse = MSE( y_test, p )
                rmse = sqrt( mse )

                print "testing RMSE:", rmse
                np.savetxt( output_predictions_file, p, fmt = '%.6f' )
