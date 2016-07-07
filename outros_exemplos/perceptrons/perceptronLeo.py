#coding: utf-8
import csv
import os
import numpy as np
import random, copy

class Perceptron2:
        x = []
        y = []
        def __init__(self,_x,_y):
                print("\n\nPerceptronLeo .............................\n\n")
                self.x = _x
                self.y = _y

                self.fit()

        def fit(self):

                #self.W=np.ones(len(self.x[0])) 
                self.W=np.ones(len(self.x[0])) #teste
                self.B=1
                
                delta = 10^5
                erro_i = 10^5
                self.l_rate = 0.8
                self.margem_de_erro = 0.05

                n = 0
                while delta > self.margem_de_erro:
                        i = 0
                        ErroTotal = 0
                        while i < len(self.x):
                                self.x[i] = np.array(self.x[i])

                                Y = 1/(1 + np.e ** - np.dot(self.W, self.x[i]) + self.B)

                                erro = np.float64(self.y[i]) - Y

                                ErroTotal = ErroTotal + abs(erro)
                                self.learn_erro(self.x[i], erro)
                                #print("----------------------------------------")
                                #print(self.W)
                                i = i + 1
                        delta = abs(erro_i - ErroTotal)
                        erro_i = ErroTotal
                        n = 1 + n

        def learn_erro(self, xi, erro):
                self.W = self.W + self.l_rate * erro * xi
                self.B = self.B + self.l_rate * erro

        def predict(self, X):
                saida = []
                
                for xi in X:
                	print(np.dot(self.W, xi))
                        #if np.dot(self.W, xi) < 0.5:
                        #        saida.append(0)
                        #else:
                        #        saida.append(1)                
                return saida