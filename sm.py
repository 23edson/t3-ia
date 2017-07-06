    ##################################################
#                                                #
#  Copyright 2009 -Marcel Pinheiro Caraciolo-    #
#  Email: caraciol@gmail.com                     #
#                                                #
#  --The Self-Organizing-maps Neural networks.   #
#  -- Version: 0.1  - 21/04/2009                 #
##################################################

"""
     Self Organizing maps neural networks - SOM Sample example.
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt

class Map(object):
    
    #Class Constructor
    #@param dimensions: Number of input dimensions
    #@param length: Length of the output grid
    #@param filePath: The file path with the input data.
    def __init__(self,dimensions,length,filePath):
        #Collection of weights
        self.outputs = []
        #Current iteration
        self.iteration = 0
        #Side length of output grid.
        self.length = length
        #Number of input dimensions
        self.dimensions = dimensions
        #Random Generator
        self.rand = random.Random()
        #Label<Patterns> dict
        self.patterns = {}
        #Initialise the SOM
        #self.initialise()
        #Load the dataset
        #self.loadData(filePath)
        #Normalise the patterns
        #self.normalisePatterns()
        #Training method
        #self.train(0.0000001)
        #Dump the coordinates
        #self.dumpCoordinates()
    
    #Initialise the Network
    def init(self,vet):
    	for i in xrange(self.length):
    		self.outputs.append([])
    		for j in xrange(self.length):
    			self.outputs[i].append(Neuron(i,j,self.length))
    			self.outputs[i][j].weights = list(vet[int(str(i)+str(j))])
    def initialise(self):
        #10x10 Dimensional Grid
        for i in xrange(self.length):
            self.outputs.append([])
            for j in xrange(self.length):
                self.outputs[i].append(Neuron(i,j,self.length))
                for k in xrange(self.dimensions):
                    self.outputs[i][j].weights.append(self.rand.random()) 
    
    #Load the dataset
    #@param filePath: The file path
    def loadD(self,vet):
    	  for line in enumerate(vet):
    	  		self.patterns[line[0]] = list(line[1])
    	  		
    	
    def loadData(self,filePath):
        fileHandle = open(filePath)
        #Ignore the first line (header)
        fileList = fileHandle.readlines()[1:]
        for line in fileList:
            line = line.strip()
            lineSet = line.split(',')
            self.patterns[lineSet[0]] = []
            for i in xrange(self.dimensions):
                self.patterns[lineSet[0]].append(float(lineSet[i+1]))
        fileHandle.close()

    #Normalise the patterns
    def normalisePatterns(self):
        for j in xrange(self.dimensions):
            sum = 0.0
            for key in self.patterns.keys():
                sum += self.patterns[key][j]
            average = sum / float(len(self.patterns))
            
            for key in self.patterns.keys():
                self.patterns[key][j] = self.patterns[key][j] / average
    
    #The training method
    #@param maxError: the error treshold
    def train(self,maxError):
        currentError = 100000.0
        
        while currentError > maxError:
            currentError = 0.0
            trainingSet = []
            for pattern in self.patterns.values():
                trainingSet.append(pattern)
            for i in xrange(len(self.patterns)):
                pattern = trainingSet[self.rand.randrange(len(self.patterns)-i)]
                currentError += self.trainPattern(pattern)
                trainingSet.remove(pattern)
                #print(i)
            
            print "Current Error: %.7f" % (currentError,)
    
    #Train Pattern
    #@param pattern: The input pattern
    def trainPattern(self,pattern):
        error = 0.0
        winner = self.winner(pattern)
        for i in xrange(self.length):
            for j in xrange(self.length):
                error += self.outputs[i][j].updateWeights(pattern,winner,self.iteration)
        
        self.iteration+=1
        
        return abs(error / (self.length * self.length))
    
    #The winner takes all rule
    #@param pattern: the input pattern
    #@return the neuron winner
    def winner(self,pattern):
        winner = None
        minD = 10000000.0
        for i in xrange(self.length):
            for j in xrange(self.length):
                d = self.distance(pattern,self.outputs[i][j].weights)
                if d < minD:
                    minD = d
                    winner = self.outputs[i][j]
        return winner

    #The euclidian distance
    #@param inVector: the input Pattern
    #@param outVector: the output neurons vector
    def distance(self,inVector,outVector):
        value = 0.0
        for i in xrange(len(inVector)):
            value +=  pow((inVector[i] - outVector[i]),2)
        
        return math.sqrt(value)
    
    #Dump the coordinates
    def dumpCoordinates(self):
        for key in self.patterns.keys():
            n = self.winner(self.patterns[key])
            print "%s,%d,%d" % (key,n.X,n.Y)
    
    
    def plotMap(self,labels):
    	
    	  fig, ax = plt.subplots()
    	  for i in range(0,10):
    	  	  for j in range(0,10):
    	  	  	   if(labels[int(str(i)+str(j))]==0):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Red")
    	  	  	   	ax.annotate(0,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black") 
    	  	  	   elif(labels[int(str(i)+str(j))]==1):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Blue")
    	  	  	   	ax.annotate(1,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==2):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Green")
    	  	  	   	ax.annotate(2,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==3):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Purple")
    	  	  	   	ax.annotate(3,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==4):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Brown")
    	  	  	   	ax.annotate(4,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==5):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Gray")
    	  	  	   	ax.annotate(5,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==6):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Gold")
    	  	  	   	ax.annotate(6,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==7):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Yellow")
    	  	  	   	ax.annotate(7,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==8):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Orange")
    	  	  	   	ax.annotate(8,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[int(str(i)+str(j))]==9):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Pink")
    	  	  	   	ax.annotate(9,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  #plt.show()	 
    def getLabels(self,testX,testY):
    	  
    	  labels = []
    	  #[(data[i] = []) for i in range(0,len(clusters))]
    	  for i in range(0,self.length):
    	  		for j in range(0,self.length):
    	  			m = 99999.8
    	  			for k in range(0,testX.shape[0]):
    	  				dist  = self.distance(testX[k],self.outputs[i][j].weights)
    	  				if(dist < m):
    	  					m = dist
    	  					winner = testY[k]
    	  				
    	 			labels.append(winner)
    	 
    	  return labels 	
 

#Simple SOM Neuron
class Neuron(object):
    #Class Constructor
    #@param x : X Coordinate
    #@param y : Y Coordinate
    #@param length: The Strength
    def __init__(self,x,y,length):
        #Neuron weights
        self.weights = []
        #X Coordinate
        self.X = x
        #Y Coordinate
        self.Y = y
        #Length 
        self.length = length
        #nf
        self.nf = 1000 / math.log(length)
    
    #Gaussian Equation
    #@param winner: The neuron winner
    #@param iteration: current iteration
    def gauss(self,winner,iteration):
        distance = math.sqrt(pow(winner.X - self.X,2) + pow(winner.Y - self.Y,2))
        
        return math.exp(-pow(distance,2) / (pow(self.strength(iteration),2)))
    
    #Set the learning rate
    #@param iteration: The current iteration 
    def learningRate(self,iteration):
        return np.exp(-iteration/1000) * 0.1
 
    #Set the strength (Neighborhood rate)
    #@param iteration : the current iteration
    def strength(self,iteration):
        return np.exp(-iteration/self.nf) * self.length
    
    #Update the weights
    #@param pattern: The input pattern
    #@param winner: The neuron winner
    #@param iteration: The current iteration
    def updateWeights(self,pattern,winner,iteration):
        sum = 0.0
        for i in xrange(len(self.weights)):
            delta = self.learningRate(iteration) * self.gauss(winner,iteration) * (pattern[i] - self.weights[i])
            self.weights[i] += delta
            sum += delta
        
        return sum / len(self.weights)

    

#####################################
#import psyco

#psyco.full()

h = np.loadtxt("rtreinada.data", delimiter=",")
treino = np.loadtxt("treino.data",delimiter=",")
teste = np.loadtxt("teste.data",delimiter=",")



#Para carregar uma rede
Xte = teste[:,:1024]
yte = teste[:,1024]
map = Map(1024,10,None)
map.init(h)  #Essa funcao carrega os pesos de uma rede treinada

labels = map.getLabels(Xte,yte) #Verifica o cluster de cada neuronio
map.plotMap(labels)
plt.show() #plota no plano xy


#Para treinar uma rede

#ESTE ALGORITMO TEM UM TREINAMENTO LENTO COM ESTE CONJUNTO
Xtr = treino[:,:1024]
ytr = treino[:,1024]
#map = Map(1024,10,None)
#map.initialise()
#map.loadD(Xtr)
#map.train(0.0001) #Erro desejado
