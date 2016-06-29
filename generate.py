#coding: utf-8
import csv
import os
import numpy as np
import random, copy

class Generate:
       
        def __init__(self,_x,_y):
                print("ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer")
                #print("\n\Analysing data ...-...\n\n")
                #X  = [] #numpy
                #x  = [] #matrix normal = array2D
                #y  = [] #array de saida = valor esperado
                #y2 = [] #dados adicionais
                X=_x
                y=_y
                
                #print("TABELA DE FEATURES:\n\n" )
                i=1
                for line in X:
                        #print(line)
                        #print (str(i)+","+str(line)+","+str(random.randint(0,4))+","+str(random.randint(0,4))+","+str(random.randint(0,4))+","+str(random.randint(0,4))+","+str(random.randint(0,4)))
                        print( "{},{},{},{},{},{}".format(i,random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),) )
                        i=i+1

                #print("SAIDA ESPERADA \n\n")
                #print(y)
                
                #print ( str(random.randint(0,4))+",",","+str(random.randint(0,4)) )
                #print (random.randint(0,4),",",random.randint(0,4),",",random.randint(0,4),",",random.randint(0,4),",",random.randint(0,4))
                #print("%d,%d,%d,%d,%d,%d" % (line,random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9) ) )

