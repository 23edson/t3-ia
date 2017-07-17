#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*   Universidade Federal da Fronteira Sul
*
*   TRABALHO III
*   Disciplina: Inteligência Artificial
*   Professor: José Carlos Bins Filho
*
*
* 	 Alunos : Edson Lemes da Silva & Lucas Cezar Parnoff
*
*
*   O trabalho consiste em executar o algoritmo para uma rede
*   de Kohonen para fazer a classificação do conjunto de dados
*   'optdigits-orig'; este conjunto é representados por exemplos
*   de dígitos em forma de bitmap. Deste modo, o algoritmo de 
*   Kohonen tenta classificar cada dígito de 0 a 9.
*
*
*   Esta biblioteca foi modificada para atender aos requisitos
*   do trabalho.
*
*   A implementação original encontra-se no endereço:
*   	http://aimotion.blogspot.com.br/2009/04/redes-neurais-auto-organizaveis-som.html
*
*
"""

import random
#import math
import numpy as np
import matplotlib.pyplot as plt
from readfile import *

class Map(object):
    
    #Class Constructor
    #@param dimensions: Quantidade de atributos
    #@param length: Quantidade de neurônios (considere-se ao quadrado)
    #@param filePath: The file path with the input data.
    def __init__(self,dimensions,length,Xtr,ytr,Xte,yte):
        #Neuronios
        self.outputs = []
        #Current iteration
        self.iteration = 0
      
        self.length = length
        
        self.dimensions = dimensions
        
        self.rand = random.Random()
        self.totalError = 0
        #conjunto de treino
        self.patterns = Xtr
        self.trainY = ytr
        self.testX = Xte
        self.testY = yte
        
        self.initialise()
        self.patterns = {}
        for line in enumerate(Xtr):
        	   self.patterns[line[0]] = list(line[1]) 
        #self.loadData(self.patterns)
        
    #Carrega os pesos de uma rede já treinada
    def loadNetwork(self,vet,labels):
    	count = 0
    	for i in range(0,self.length):
    		self.outputs.append([])
    		for j in range(0,self.length):
    			#self.outputs[i].append(Neuron(i,j,self.length))
    			self.outputs[i][j].weights = list(vet[count])
    			self.outputs[i][j].setLabel(labels[count])
    			count+=1
    #Inicializa os pesos de cada neuronio randomicamente			
    def initialise(self):
        #10x10 Dimensional Grid
        for i in range(0,self.length):
            self.outputs.append([])
            for j in range(0,self.length):
                self.outputs[i].append(Neuron(i,j,self.length))
                for k in range(0,self.dimensions):
                    self.outputs[i][j].weights.append(self.rand.random()) 
    
    #Carrega o conjunto de treino
    #def loadData(self,vet):
    #	  self.patterns = vet
    	  		
    #Função de treinamento
    #@param maxError: condição de parada 
    def train(self,maxError,flag=False):
        currentError = 100000.0
        
        while currentError > maxError:
            currentError = 0.0
            trainingSet = []
            trainingLabel = self.trainY
            for pattern in self.patterns.values():
            	trainingSet.append(pattern)
            #s = np.arange(trainingSet.shape[0])
            #np.random.shuffle(s)
            #'embaralha' os exemplos
            #np.random.shuffle(trainingSet)
            for i in range(0,len(trainingSet)):
            	choice = self.rand.randrange(len(self.patterns)-i)
            	pattern = trainingSet[choice]
            	#currentError += self.trainPattern(trainingSet[s][i],flag,trainingLabel[s][i])
            	currentError += self.trainPattern(pattern,flag,trainingLabel[choice])
            	if(flag==True):
            		print("Exemplo: " + str(i) + " escolhido, rotulo:" + str(int(self.trainY[i])))
               
            print("Erro atual: %.7f" % (currentError,))
            #labels = self.getLabels(self.Xte,self.yte)
            #self.plotMap(labels)
            #plt.show()
        
        self.totalError = maxError
            
    
    #Atualização em relação a um exemplo específico
    def trainPattern(self,pattern,flag,label):
        error = 0.0
        
        winner = self.winner(pattern)
        if(flag==True):
           print("Neuronio vencedor: posicao :" + "x:"+str(winner.X) + " y:" + str(winner.Y) )
        for i in range(0,self.length):
            for j in range(0,self.length):
                error += self.outputs[i][j].updateWeights(pattern,winner,self.iteration)
        if(flag==True):        
           print("Atualizacao para este exemplo terminou\n")
        self.iteration+=1
        winner = self.winner(pattern)
        winner.setLabel(label) 
        #Devolve o erro em relação a atualização dos pesos
        return abs(error / (self.length * self.length))
    
    #Verifica o neuronio vencedor, isto é
    #Aquele com a menor distancia euclidiana em relação a um exemplo
    def winner(self,pattern):
        winner = None
        minD = 10000000.0
        for i in range(0,self.length):
            for j in range(0,self.length):
                d = self.distance(pattern,self.outputs[i][j].weights)
                if d < minD:
                    minD = d
                    winner = self.outputs[i][j]
        return winner

    #Distancia euclidiana
    #@param inVector: Exemplo analisado
    #@param outVector: vetor de pesos 
    def distance(self,inVector,outVector):
        value = 0.0
        for i in range(0,len(inVector)):
            value +=  pow((inVector[i] - outVector[i]),2)
        
        return value
   
    #Atribui uma cor para cada classe diferente para plotar em um plano xy
    #@param labels: classe de cada neurônio
    def plotMap(self,labels):
    	
    	  fig, ax = plt.subplots()
    	  
    	  count = 0
    	  for i in range(0,self.length):
    	  	  for j in range(0,self.length):
    	  	  	   if(labels[count]==0):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Red")
    	  	  	   	ax.annotate(0,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black") 
    	  	  	   elif(labels[count]==1):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Blue")
    	  	  	   	ax.annotate(1,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==2):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Green")
    	  	  	   	ax.annotate(2,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==3):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Purple")
    	  	  	   	ax.annotate(3,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==4):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Brown")
    	  	  	   	ax.annotate(4,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==5):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Gray")
    	  	  	   	ax.annotate(5,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==6):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,c=40)
    	  	  	   	ax.annotate(6,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==7):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Yellow")
    	  	  	   	ax.annotate(7,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==8):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Orange")
    	  	  	   	ax.annotate(8,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   elif(labels[count]==9):
    	  	  	   	ax.scatter(self.outputs[i][j].X,self.outputs[i][j].Y,color="Pink")
    	  	  	   	ax.annotate(9,(self.outputs[i][j].X,self.outputs[i][j].Y),color="Black")
    	  	  	   count+=1
    	  #plt.show()
    
    #Verifica os rotulos de cada neuronio
    #@param testX : conjunto de teste
    #@param testY : rótulos do conjunto de teste	 
    def getLabels(self):
    	  
    	  labels = []
    	  #[(data[i] = []) for i in range(0,len(clusters))]
    	  for i in range(0,self.length):
    	  		for j in range(0,self.length):
    	  			m = 99999.8
    	  			for k in range(0,self.testX.shape[0]):
    	  				dist  = self.distance(self.testX[k],self.outputs[i][j].weights)
    	  				if(dist < m):
    	  					m = dist
    	  					winner = self.testY[k]
    	  			labels.append(winner)
    	 
    	  return labels
    	  
    def classify(self,header):
    	   actual = []
    	   for i in range(0,self.length):
    	   	for j in range(0,self.length):
    	   		actual.append(self.outputs[i][j].getLabel())
    	   labels = self.getLabels()
    	   self.plotMap(actual)
    	   if(header==None):
    	   	print("Esta rede foi treinada com: " + str(self.length*self.length)+ " neuronios, Erro de:" + str(self.totalError))
    	   else:print("Esta rede foi treinada com: " + str(header[0]*header[0]) + " neuronios, Erro de: " + str(header[1]))
    	   print("Porcentagem de acerto:" + str(100*np.mean(np.array(labels)==np.array(actual)))+"%")
    	   
    	   #plt.show() 
    
    #Salva a rede em um arquivo
    #@param name: nome do arquivo a ser salvo	  
    def saveNetwork(self,name):
    	  out = np.array(self.outputs[0][0].weights)
    	  labels = []
    	  labels.append(self.outputs[0][0].getLabel())
    	  for i in range(1,self.length):
    	  	   out = np.vstack([out,np.array(self.outputs[0][i].weights)])
    	  	   labels.append(self.outputs[0][i].getLabel())
    	  for i in range(1,self.length):
    	  	   for j in range(0,self.length):
    	  	   	 out = np.vstack([out,np.array(self.outputs[i][j].weights)])
    	  	   	 labels.append(self.outputs[i][j].getLabel())
    	  header = "#"+str(self.length) + "#" + str(self.totalError)
    	  np.savetxt(name,out,delimiter=",",header=str(header))
    	  np.savetxt("l"+name,np.array(labels),delimiter=",")

#Representa um neurônio
class Neuron(object):
    #Class Constructor
    #@param x : X Coordinate
    #@param y : Y Coordinate
    #@param length: The Strength
    def __init__(self,x,y,length):
        #pesos
        self.weights = []
        
        #coordenada X
        self.X = x
        self.label = 0
        #coordenada Y
        self.Y = y
        
        #quantidade de neuronios na rede 
        self.length = length
        #sigma inicial
        self.nf = 1000 / np.log(length)
    
    #Influencia da vizinhança
    #@param winner: neuronio vencedor
    #@param iteration: iteracao atual
    def gauss(self,winner,iteration):
        distance = (pow(winner.X - self.X,2) + pow(winner.Y - self.Y,2))
        
        return np.exp(-pow(distance,2) / (pow(self.strength(iteration),2)))
    
    #Atualiza a taxa de aprendizagem
    #@param iteration: iteração atual do algoritmo 
    def learningRate(self,iteration):
        return np.exp(-iteration/1000) * 0.1
 
    def setLabel(self,num):
    	  self.label = num
    def getLabel(self):
    	  return self.label
    #Atualiza a taxa de "força" da vizinhança(raio)
    #@param iteration : iteração atual
    def strength(self,iteration):
        return np.exp(-iteration/self.nf) * self.length
    
    #Atualiza os pesos
    #@param pattern: Exemplo a ser avaliado
    #@param winner: Neurônio vencedor
    #@param iteration: iteração atual
    def updateWeights(self,pattern,winner,iteration):
        sum = 0.0
        for i in range(0,len(self.weights)):
            delta = self.learningRate(iteration) * self.gauss(winner,iteration) * (pattern[i] - self.weights[i])
            self.weights[i] += delta
            sum += delta
        
        return sum / len(self.weights)

