#coding: utf-8

import csv
import os
import numpy as np

import random, copy

#os.system('cls')
# 0
# AnimalID   

# 1         2           3           4               5           6               7               8       9
# Name    DateTime    OutcomeType OutcomeSubtype  AnimalType SexuponOutcome  AgeuponOutcome  Breed   Color
#   3       x           5           16              2           2   + 3            9999         2       2


#-------------------------PrepareData 
class PrepareData:
    X  = [] #numpy
    x  = [] #matrix normal = array2D
    y  = [] #array de saida = valor esperado
    y2 = [] #dados adicionais
    def __init__(self,file):
        print("Preparando data .............................")
        # self.x.append("zero")
        #self.x.extend(["AnimalID","Name","DateTime","AnimalType","SexuponOutcome","AgeuponOutcome","Breed","Color"])
        #print( self.x[0:8])

        with open(file, 'r') as csv_file:
            train = csv.reader(csv_file, delimiter=',')
            end=0
            for i, row in enumerate(train):
                if i != 0: 

                    self.y.append ( self.OutcomeType(row[3]) )
                    #self.y2.append ( self.OutcomeSubtype(row[4]) )

                    
                    #criar o numpy part 1/2
                    '''
                    #print ( "\n")
                    self.x.extend ( [row[0]]) ##remover
                    self.x.extend ( [self.Name(row[1])])
                    self.x.extend ( [self.Date(row[2])])
                    self.x.extend ( [self.AnimalType(row[5])])
                    self.x.extend ( [self.SexuponOutcome1(row[6])] )
                    self.x.extend ( [self.SexuponOutcome2(row[6]) ])
                    self.x.extend ( [self.AgeuponOutcome(row[7])] )
                    self.x.extend ( [self.Breed(row[8]) ])
                    self.x.extend ( [self.Color1(row[9])] )
                    self.x.extend ( [self.Color2(row[9]) ] )
                    '''

                    #criar matrix comum = array de 2 dimensoes
                    self.x.append( [self.Name(row[1]) , self.Date([row[2]]), self.AnimalType(row[5]) , self.SexuponOutcome1(row[6]) , self.SexuponOutcome2(row[6]) , self.AgeuponOutcome(row[7]) , self.Breed(row[8])  , self.Color1(row[9]) , self.Color2(row[9]) ])
 
               #endif
            #endfor 
        #endwith
        
        #self.X=np.array(x).reshape(len(x)/9,9) #criar o numpy part 2/2
        #self.Printer(len(x)/9) #printar o numpy part

    #end__init__

    def Printer(self,lines):
        for i in xrange(lines):
            print(self.X[i]) #matrix
            print(self.y[i]) #retorno_esperado #OutcomeType
            print(self.y2[i]) #retorno_esperado2 #OutcomeSubType
            print("\n")


    #SWITCHS
    #http://www.pydanny.com/why-doesnt-python-have-switch-case.html
    def Name(self,value):
    	
        if value is '':
            return 1
        else:
            return 2

    def Date(self,value):
        return 2
        """
        day    = value.split("-")[2]
        month  = value.split("-")[1]
        hour   = value.split(":")[-3].split(" ")[-1]
        minute = value.split(":")[-2]

        print(value,day,month,hour,minute)

        if month==12:
            if (day==25 or day==31):
                return 1
        if month==5:
            if (day<5):
                return 1
        if month==12:
            if (day==25 or day==31):
                return 1
        return 2
        """


    def OutcomeType(self, value):
        options = {
            'Return_to_owner': 1,
            'Euthanasia': 2,
            'Adoption': 3,
            'Transfer': 4,
            'Died': 5
        }

        return options.get(value,-1)


    def AnimalType(self, value):
        options = {
            'Dog': 1,
            'Cat': 2
        }
        #print ( value)
        return options.get(value,-1)


    def SexuponOutcome1(self, value):
        options = {
            'Intact': 1,
            'Spayed': 2,
            'Neutered': 3,
            'Unknown': 4
        }
        
        #print ( value.split(" ")[0] )
        return options.get(value.split(" ")[0],-1)


    def SexuponOutcome2(self, value):

        if value.endswith("Male"):
            #print ( "Male" )
            return 1
        else:
            #print ( "Female" )
            return 2


    def AgeuponOutcome(self, value):
        
        if value is '': 
            return -1
        else:
            number = value.split(" ")[0]
            string = value.split(" ")[-1]

            if string.startswith("year"):
                number=int(number)*365
            elif string.startswith("month"):
                number=int(number)*30
            elif string.startswith("weeks"):
                number=int(number)*7
            
            #print ( number )
            return number
       

    def Breed (self, value):
        if value.endswith("Mix"):
            #print ( "Mix" )
            return 0
        else:
            #print ( "Pure" )
            return 1


    def Color1 (self, value):
        #print ( value.split("/")[0] )
        #return value.split("/")[0]
        options = {
            'Black': 10,
            'Blue': 1,
            'Brown': 2,
            'Gray': 3,
            'Orange': 4,
            'Red': 5,
            'Sable': 6,
            'Tan': 7,
            'Tricolor': 8,
            'White': 9
        }
        return options.get( value.split("/")[0], -1)


    def Color2 (self, value):
        #print ( value.split("/")[1:] )
        #color2 = value.split("/")[1:] //como tratar se nao existe?
        #color1,color2 = value.split("/") //como tratar se nao existe?
        #solucao1:

        if value.split("/")[0] == value.split("/")[-1]:
            return 1
        else:
            #return value.split("/")[-1]
            return 2

