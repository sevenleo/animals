#coding: utf-8
import csv
import os

#os.system('cls')
# 0
# AnimalID   

# 1         2           3           4               5           6               7               8       9
# Name    DateTime    OutcomeType OutcomeSubtype  AnimalType SexuponOutcome  AgeuponOutcome  Breed   Color
#   3       x           5           16              2           2   + 3            9999         2       2
 
class PrepareData:

    x = []
    y_ = []

    def __init__(self,file):
        with open(file, 'r') as csv_file:
            train = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(train):
                if i != 0: 
                    xi = [] 

                    print ( "\n")
                    xi.append (row[0]) ##remover
                    xi.append ( self.Name(row[1]) )
                    xi.append ( self.OutcomeType(row[3]) )
                    xi.append ( self.OutcomeSubtype(row[4]) )
                    xi.append ( self.AnimalType(row[5]) )
                    xi.append ( self.SexuponOutcome1(row[6]) )
                    xi.append ( self.SexuponOutcome2(row[6]) )
                    xi.append ( self.AgeuponOutcome(row[7]) )
                    xi.append ( self.Breed(row[8]) )
                    xi.append ( self.Color1(row[9]) )
                    xi.append ( self.Color2(row[9])  )
                    print ( xi)



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