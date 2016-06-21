#coding: utf-8
import csv
import os
import numpy as np

#os.system('cls')
# 0
# AnimalID   

# 1         2           3           4               5           6               7               8       9
# Name    DateTime    OutcomeType OutcomeSubtype  AnimalType SexuponOutcome  AgeuponOutcome  Breed   Color
#   3       x           5           16              2           2   + 3            9999         2       2
 
class PrepareData:



    def __init__(self,file):
        x = []
        #x.append("zero")
        #x.extend(["AnimalID","Name","DateTime","AnimalType","SexuponOutcome","AgeuponOutcome","Breed","Color"])
        #print(x[0:8])
        y = []
        y2 = []

        with open(file, 'r') as csv_file:
            train = csv.reader(csv_file, delimiter=',')
            end=0
            for i, row in enumerate(train):
                if i != 0: 
                    #print ( "\n")

                    y.append ( self.OutcomeType(row[3]) )
                    y2.append ( self.OutcomeSubtype(row[4]) )

                    x.extend ( [row[0]]) ##remover
                    x.extend ( [self.Name(row[1])])
                    x.extend ( [self.AnimalType(row[5])])
                    x.extend ( [self.SexuponOutcome1(row[6])] )
                    x.extend ( [self.SexuponOutcome2(row[6]) ])
                    x.extend ( [self.AgeuponOutcome(row[7])] )
                    x.extend ( [self.Breed(row[8]) ])
                    x.extend ( [self.Color1(row[9])] )
                    x.extend ( [self.Color2(row[9]) ] )
                    
                    #start   = end
                    #end    = start+9
                    #print(x[start:end])
                    #print("OutcomeType:", y[i-1])
                    #print("OutcomeSubType:", y2[i-1])
                #endif
            #endfor 
        #endwith
        X=np.array(x).reshape(len(x)/9,9)

        for i in xrange(len(x)/9):
            print(X[i]) #matrix
            print(y[i]) #retorno_esperado #OutcomeType
            print(y2[i]) #retorno_esperado2 #OutcomeSubType
            print("\n")

        

    #endinit


#SWITCHS
#http://www.pydanny.com/why-doesnt-python-have-switch-case.html
    def Name(self,value):
        if value is '':
            return 
        else:
            return 0

    def OutcomeType(self, value):
        options = {
            'Return_to_owner': 0,
            'Euthanasia': 1,
            'Adoption': 2,
            'Transfer': 3,
            'Died': 4
        }

        return options.get(value,"NaN")


    def OutcomeSubtype(self, value):
        options = {
            'Suffering': 0,
            'Foster': 1,
            'In Foster': 1,
            'Partner': 2,
            'Offsite': 3,
            'SCRP': 4,
            'Aggressive': 5,
            'Behavior': 6,
            'Medical': 7,
            'Rabies Risk': 8,
            'In Kennel': 9,
            'Enroute': 10,
            'At Vet': 11,
            'In Surgery': 12,
            'Barn': 13,
            'Court/Investigation': 14,
            '': 15
        }
        #print ( value)
        return options.get(value,"NaN")


    def AnimalType(self, value):
        options = {
            'Dog': 0,
            'Cat': 1
        }
        #print ( value)
        return options.get(value,"NaN")


    def SexuponOutcome1(self, value):
        options = {
            'Intact': 0,
            'Spayed': 1,
            'Neutered': 2,
            'Unknown': 3
        }
        
        #print ( value.split(" ")[0] )
        return options.get(value.split(" ")[0],"NaN")
        #return "Intact, Spayed, Neutered, Unknown"


    def SexuponOutcome2(self, value):

        if value.endswith("Male"):
            #print ( "Male" )
            return 0
        else:
            #print ( "Female" )
            return 1

    def AgeuponOutcome(self, value):
        
        if value is '': 
            return 0
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
            return 1
        else:
            #print ( "Pure" )
            return 0


    def Color1 (self, value):
        #print ( value.split("/")[0] )
        return value.split("/")[0]


    def Color2 (self, value):
        #print ( value.split("/")[1:] )
        #color2 = value.split("/")[1:] //como tratar se nao existe?
        #color1,color2 = value.split("/") //como tratar se nao existe?
        #solucao1:

        if value.split("/")[0] == value.split("/")[-1]:
            return 
        else:
            return value.split("/")[-1]



#========================= MAIN.EXEC =========================#

microtrain =  "microtrain.csv"   
train = "../data/shelter_animal/train.csv"
train = "train.csv"
test = "../data/shelter_animal/test.csv"
PrepareData(microtrain)




#=========================comentarios=========================#


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