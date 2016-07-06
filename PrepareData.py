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
    testx = []

    def __init__(self,file):
        print("Preparando data .........")
        agemin,agemax = self.NormalizarIdades(file,False)    
        with open(file, 'r') as csv_file:
            train = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(train):
                if i != 0: 
                    self.y.append ( self.OutcomeType(row[3]) )
                    #self.y2.append ( self.OutcomeSubtype(row[4]) )
                    self.x.append( [self.Name(row[1]) , self.Date([row[2]]),self.Hour([row[2]]),self.Minute([row[2]]),self.Month([row[2]]),self.Day([row[2]]),self.AnimalType(row[5]) , self.SexuponOutcome1(row[6]) , self.SexuponOutcome2(row[6]) , self.AgeuponOutcome(row[7],agemin,agemax) , self.Breed(row[8])  , self.Domestic (row[8]),self.Miniature(row[8]),self.Longhair (row[8]),self.Shorthair(row[8]),self.Wirehair (row[8]), self.Color1(row[9]) , self.Color2(row[9]) ])
               #endif
            #endfor 
        #endwith


    def PrepareTestFile(self,file):
        with open(file, 'r') as csv_file:
                agemin,agemax = self.NormalizarIdades(file,True)    
                train = csv.reader(csv_file, delimiter=',')
                for i, row in enumerate(train):
                    if i != 0: 
                        self.testx.append([self.Name(row[1]) , self.Date([row[2]]), self.Hour([row[2]]),self.Minute([row[2]]),self.Month([row[2]]),self.Day([row[2]]),self.AnimalType(row[3]) , self.SexuponOutcome1(row[4]) , self.SexuponOutcome2(row[4]) , self.AgeuponOutcome(row[5],agemin,agemax) , self.Breed(row[6]),self.Domestic (row[6]),self.Miniature(row[6]),self.Longhair (row[6]),self.Shorthair(row[6]),self.Wirehair (row[6]), self.Color1(row[7]) , self.Color2(row[7]) ])
                    #endif
                #endfor 
            #endwith
        return self.testx

    #end__init__
    def NormalizarIdades(self,file,isTestFile):
        min=99999999999
        max=-99999999999
        with open(file, 'r') as csv_file:
                train = csv.reader(csv_file, delimiter=',')
                for i, row in enumerate(train):
                    if i != 0:
                        if isTestFile==False:
                            idade = self.AgeuponOutcomeMinMax(row[7]) 
                            if( idade < min):
                                min = idade
                            if (idade > max):
                                max = idade
                        else:
                            idade = self.AgeuponOutcomeMinMax(row[5]) 
                            if( idade < min):
                                min = idade
                            if (idade > max):
                                max = idade
        return [min,max]


    #funcao auxiliar   
    def AgeuponOutcomeMinMax(self, value):
        
        if value is '': 
            return -1
        else:
            number = value.split(" ")[0]
            string = value.split(" ")[-1]

            number=int(number)
            
            if string.startswith("year"):
                number=int(number)*365
            elif string.startswith("month"):
                number=int(number)*30
            elif string.startswith("weeks"):
                number=int(number)*7
            #print ( number )
            return number
       


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
            return 0
        else:
            return 1

    def Hour(self,value):
        date = "".join(value)
        hour   = float(date.split(":")[-3].split(" ")[-1])
        return float(hour/24.0)

    def Minute(self,value):
        date = "".join(value)
        minute = float(date.split(":")[-2])
        return float(minute/60.0)
    
    def Month(self,value):
        date = "".join(value)
        month  = float(date.split("-")[1])
        return float(month/12.0)
    
    def Day(self,value):
        date = "".join(value)
        day  = float(date.split("-")[2].split(" ")[0])
        return float(day/31.0)

    def Date(self,value):
        date = "".join(value)

        day    = date.split("-")[2].split(" ")[0]
        month  = date.split("-")[1]
        hour   = date.split(":")[-3].split(" ")[-1]
        minute = date.split(":")[-2]


        if month==12:
            if (day==25 or day==31):
                return 0
        elif month==5:
            if (day<5):
                return 0
        elif month==12:
            if (day==25 or day==31):
                return 0
        else:
            return 1


    #ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer
    def OutcomeType(self, value):
        options = {
            'Adoption': 0,
            'Died': 1,
            'Euthanasia': 2,
            'Return_to_owner': 3,
            'Transfer': 4
        }

        return options.get(value,0)


    def AnimalType(self, value):
        options = {
            'Dog': 0,
            'Cat': 1
        }
        #print ( value)
        return options.get(value,0)


    def SexuponOutcome1(self, value):
        options = {
            'Unknown': 0,
            'Intact': 1,
            'Spayed': 2,
            'Neutered': 2
        }
        
        #print ( value.split(" ")[0] )
        return float (options.get(value.split(" ")[0],0)/2.0)


    def SexuponOutcome2(self, value):

        if value.endswith("Male"):
            #print ( "Male" )
            return 0
        else:
            #print ( "Female" )
            return 1


    def AgeuponOutcome(self, value, min, max):
        
        if value is '': 
            return 0.5
        else:
            number = value.split(" ")[0]
            string = value.split(" ")[-1]

            number=int(number)
            
            if string.startswith("year"):
                number=int(number)*365
            elif string.startswith("month"):
                number=int(number)*30
            elif string.startswith("weeks"):
                number=int(number)*7
            

            #saida de 0 a 1            
            number = (float(number) - float(min))/float(max)
            return number
            #return float("{0:.3f}".format(number))
       



    def Breed (self, value):
        #soma com impares evita problemas de valores iguais ao acaso
        if "Mix" in value:
            #print ( "Mix" )
            return 0
        elif "/" in value:
            #print ( "Mix" )
            return 0
        else:
            #print ( "Pure" )
            return 1

    def Domestic (self, value):
        if "Domestic" in value:
            return 0
        else:
            return 1

    def Miniature(self, value):
        if "Miniature" in value:
            return 0
        else:
            return 1
        
    def Longhair (self, value):
        if "Longhair" in value:
            return 0
        else:
            return 1

    def Shorthair (self, value):
        if "Shorthair" in value:
            return 0
        else:
            return 1

    def Wirehair (self, value):
        if "Wirehair" in value:
            return 0
        else:
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
        return float (options.get( value.split("/")[0], 0)/10.0)

    def Color2 (self, value):
        if value.split("/")[0] == value.split("/")[-1]:
            return 0
        else:
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
            return float (options.get( value.split("/")[-1], 11)/12.0)




"""
Separar as raças populares para adocao.

Raças disponiveis (sem mixes):
Airedale Terrier
Akita
American Bulldog
American Pit Bull Terrier
American Staffordshire Terrier
Anatol Shepherd
Angora
Australian Cattle Dog
Australian Shepherd
Basset Hound
Beagle
Bernese Mountain Dog
Black
Black Mouth Cur
Blue Lacy
Border Collie
Border Terrier
Boxer
Breed
Cairn Terrier
Cardigan Welsh Corgi
Catahoula
Chesa Bay Retr
Chihuahua Longhair
Chihuahua Shorthair
Chinese Sharpei
Chow Chow
Cocker Spaniel
Collie Smooth
Dachshund
Dachshund Longhair
Dachshund Wirehair
Doberman Pinsch
Dogo Argentino
Dogue De Bordeaux
Domestic Longhair
Domestic Medium Hair
Domestic Shorthair
English Bulldog
English Foxhound
English Pointer
Exotic Shorthair
Flat Coat Retriever
German Shepherd
Great Dane
Great Pyrenees
Italian Greyhound
Jack Russell Terrier
Labrador Retriever
Lhasa Apso
Maltese
Manchester Terrier
Manx
Miniature Pinscher
Miniature Poodle
Miniature Schnauzer
Norfolk Terrier
Pit Bull
Plott Hound
Pointer
Queensland Heeler
Rat Terrier
Rhod Ridgeback
Rottweiler
Russian Blue
Scottish Terrier
Shetland Sheepdog
Shih Tzu
Siamese
Siberian Husky
Tan Hound
Tibetan Terrier
Treeing Walker Coonhound
Vizsla
Whippet
Yorkshire Terrier
Yorkshire Terrier 
"""