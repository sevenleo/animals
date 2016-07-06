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


from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

class Generate:
       
        def __init__(self,_x,_y):
                print("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer")


        
        def random(self):
                X=_x
                y=_y
                i=1
                for line in self.X:
                        print( "{},{},{},{},{},{}".format(i,random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),) )
                        i=i+1                
        

        def train(self,train_file):
                #treino de regressao ML

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


        def ReadTrainFile(self,_x,_y):
                 #prepara um banco de dados com as proporcoes dos arquivos de entrada _x e _y
                TrainData = ClassificationDataSet(len(_x[0]), 1, nb_classes=5)

                #insere os exemplos
                i=0
                for line in _x:
                        #input = multivariate_normal(means[klass],cov[klass])
                        #print(line)
                        TrainData.addSample(line, _y[i])
                        i+=1

                return TrainData

        def ReadTestFile(self,test_file,features):
                TestData = ClassificationDataSet(features, 1, nb_classes=5)               
                i=0
                for line in open(test_file, 'r'):
                        nline = np.fromstring(line, dtype=int, sep=',')
                        TestData.addSample(nline, -1)
                        i+=1
                return TestData



        def predict_class(self,_x,_y,test_file):
                #estatistica
                acertos =0
                erros=0

                
                #separa uma parte do treino para teste   
                #testdata, traindata = TrainData.splitWithProportion( 0.1 )

                traindata = self.ReadTrainFile(_x,_y)
                testdata = self.ReadTestFile( test_file, len(_x[0]) )

                traindata._convertToOneOfMany( )
                testdata._convertToOneOfMany( )

                """
                print "____________________________________________________________________________"
                print "Number of training patterns: ", len(traindata)
                print "Input and output dimensions: ", traindata.indim, traindata.outdim
                print "First sample (input, target, class):"
                print traindata['input'][0], traindata['target'][0], traindata['class'][0]
                print "____________________________________________________________________________\n"

                """

                fnn = buildNetwork( traindata.indim, 5, traindata.outdim, outclass=SoftmaxLayer )
                trainer = BackpropTrainer( fnn, dataset=traindata, momentum=0.1, verbose=True, weightdecay=0.01)

                """
                ticks = arange(-3.,6.,0.2)
                X, Y = meshgrid(ticks, ticks)

                # need column vectors in dataset, not arrays
                griddata = ClassificationDataSet(2,1, nb_classes=3)
                for i in xrange(X.size):
                    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
                griddata._convertToOneOfMany()  # this is still needed to make the fnn feel comfy
                
                """
                for i in range(2):
                        trainer.trainEpochs( 1 )

                for i in xrange(0,len(testdata)):
                        '''
                        a=int(testdata['target'][i][0])
                        b=int(testdata['target'][i][1])
                        c=int(testdata['target'][i][2])
                        d=int(testdata['target'][i][3])
                        e=int(testdata['target'][i][4])


                        res=-1
                        if (a==1):
                        res+=1
                        elif (b==1):
                        res+=2
                        elif (c==1):
                        res+=3
                        elif (d==1):
                        res+=4
                        elif (e==1):
                        res+=5
                        '''

                        if ( _y[i] != testdata['class'][i] ):
                                erros+=1
                        else:
                                acertos+=1

                        print("Exemplo - ", i)
                        print testdata['target'][i]
                        #print ("classe: {}".format(res) )
                        print ("saida:  {}".format(int(testdata['class'][i])) ) 
                        print ("____________________________" )

                print("acertos:  " , acertos)
                print("erros:    ", erros)

                if ( acertos+erros == len(_x) ):
                        print("Teste Completo")
                else:
                        print("****** Teste Falho")
                        print(len(_x))
                