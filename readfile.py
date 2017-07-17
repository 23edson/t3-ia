#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
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
*   Este arquivo permite fazer a leitura do conjunto e a separacao
*   entre conjunto de treino e teste. E tambem a leitura de redes salvas
*   em arquivos externos

'''

import numpy as np
#from mvpa2.suite import *

tam = 1934

#Le o arquivo original
def readFile(name):
	
	fl = open(name)
	for i in range(0,tam):
		
		#arr = np.zeros((1,(tam*tam)+1),dtype="float")
		a = fl.read(1056)
		b = fl.read(3)
		a = a.split("\n")
		
		lt = list(a[0])
		for j in range(1,len(a)-1):
			lt = lt + list(a[j])
			
		lt = lt + (list(b.strip()))
		if(i == 0):
			arr = np.array(lt,dtype="float")
		else:
			arr = np.vstack([arr,np.array(lt,dtype="float")])
	
	fl.close()	
	return arr
	
#Divide o conjunto original em conj de treino e teste (70% e 30% respectivamente)
def divideSet(arq):
	X = arq[:,:1024]
	y = arq[:,1024]
	
	Xtr = X[0:int(X.shape[0]*0.7),:]
	ytr = y[0:int(X.shape[0]*0.7)]
	
	Xte = X[int(X.shape[0]*0.7):-1:,]
	yte = y[int(X.shape[0]*0.7):-1]
	
	return Xtr,ytr,Xte,yte
	
#Carrega os pesos de uma rede ja treinada, juntamente com os dados sobre essa rede
def loadWeights(name):
	h = np.loadtxt(name,delimiter=",")
	h1 = np.loadtxt("l"+name,delimiter=",")
	arq = open(name)
	g= arq.readline()
	arq.close()
	g= g.strip()
	g=g.split("#")
	header = []
	header.append(int(g[2]))
	header.append(float(g[3]))
	
	return h,h1,header



