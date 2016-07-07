#coding: utf-8
import csv
import ast
import os
import numpy as np
import random, copy
import cPickle as pickle
from math                           import sqrt
from sklearn.metrics                import mean_squared_error as MSE
from pybrain.datasets.supervised    import SupervisedDataSet as SDS
from pybrain.tools.shortcuts        import buildNetwork
from pybrain.supervised.trainers    import BackpropTrainer
from pybrain.tools.shortcuts        import buildNetwork

#from pybrain.tools.customxml        import NetworkWriter
#from pybrain.tools.customxml        import NetworkReader
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

from pybrain.datasets               import ClassificationDataSet
from pybrain.utilities              import percentError
from pybrain.tools.shortcuts        import buildNetwork
from pybrain.supervised.trainers    import BackpropTrainer
from pybrain.structure.modules      import SoftmaxLayer
from pylab                          import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy                          import diag, arange, meshgrid, where
from numpy.random                   import multivariate_normal

class Generate:
       
        def __init__(self,_x,_y):
                print("funcao Generacao .............. ")
                #print("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer")

        
        def random(self,lines):
                print("Criando dados aletatorios .... ")
                i=1
                output = open('animal_output_RANDOM.csv', 'wb')
                output.write("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer\n") 
                for line in xrange(lines):
                        output.write( "{},{},{},{},{},{}\n".format(i,random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),) )
                        i=i+1                
                print("Concluido. Verifique o arquivo animal_output_RANDOM.csv")
        

        """
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
        """

        """
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
        """


        #http://pybrain.org/docs/tutorial/fnn.html

        def ReadTrainFile(self,_x,_y):
                print("Lendo matriz de treino .......")
                 #prepara um banco de dados com as proporcoes dos arquivos de entrada _x e _y
                TrainData = ClassificationDataSet(len(_x[0]), 1, nb_classes=5)

                #insere os exemplos
                i=0
                for line in _x:
                        TrainData.addSample(line, _y[i])
                        i+=1
                return TrainData



        def ReadTestFile(self,test_file,features):
                print("Lendo arquivo de teste ........")
                TestData = ClassificationDataSet(features, 1, nb_classes=5)               
                i=0
                test = open(test_file, 'r')
                for line in test:
                        nline = np.fromstring(line, dtype=int, sep=',')
                        TestData.addSample(nline, -1)
                        i+=1
                test.close()        
                return TestData



        def predict_class(self,_x,_y,test_file,epochs,steps):
                print("Iniciando funcao predict_class() .............")


                traindata = self.ReadTrainFile(_x,_y)
                #testdata = self.ReadTestFile( test_file, len(_x[0]) )
                
                print ("____________________________________________________________________________")
                print ("A matrix de treino tem ", len(traindata),"linhas de dados")
                print ("Dimensoes de Input e Output : ", traindata.indim, traindata.outdim)
                print ("____________________________________________________________________________\n")
                

                print("convertendo arquivos .................")

                traindata._convertToOneOfMany( )
                #testdata._convertToOneOfMany( )

                import os.path
                if os.path.exists('rede_animal.xml'):
                    print(" Carregando a rede de treinos do arquivo rede_animal.xml *************** ")
                    fnn = NetworkReader.readFrom('rede_animal.xml')
                else:
                    print(" Criando rede de treinos no arquivo rede_animal.xml *************** ")
                    fnn = buildNetwork( traindata.indim, 5, traindata.outdim, outclass=SoftmaxLayer )

                trainer = BackpropTrainer( fnn, dataset=traindata, momentum=0.1, verbose=True, weightdecay=0.01)

                print("Treinando .............")
                
                for i in range(epochs):
                        print("Treinando epoca ", i)
                        trainer.trainEpochs( steps )
                        NetworkWriter.writeToFile(fnn, 'rede_animal.xml')
                        print(" Rede salva em rede_animal.xml (Ok) ")

                print("Lendo arquivo de teste e classificando ..........")
                print("Gerando resultados em ANIMAL_OUTPUT.CSV ..........")
                output = open('animal_output.csv', 'wb')
                i=1
                output.write("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer\n")
                for line in open(test_file, 'r'):
                        x = ast.literal_eval(line)
                        output.write( "{},{},{},{},{},{} \n".format(i,fnn.activate( x )[0],fnn.activate( x )[1],fnn.activate( x )[2],fnn.activate( x )[3],fnn.activate( x )[4]) )
                        i=i+1   
                print("Concluido")

                