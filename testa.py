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
*   Este é um arquivo exemplo de como carregar uma rede já treinada.
*   Deste modo, é feito a leitura do conjunto de dados, a
*   separação entre conjunto de treino e teste, o carregamento da rede,
*   a classificação do conjunto de teste e finalmente a apresentação do
*   resultado.

'''

from som import *

#Carrega o conjunto original de dados
conj = readFile("optdigits.data")

#Divide o conjunto em treino e teste com seus rotulos
Xtr,ytr,Xte,yte = divideSet(conj)


#Carrega uma rede treinada no vetor weights, header representa os dados sobre a rede carregada
#@param: nome do arquivo onde esta a rede treinada
weights,labels,header = loadWeights("rtreinada.data")

#Carrega outra rede
weights2,labels2, header2 = loadWeights("rtreinada1.data")

#Cria uma instancia da classe Map
#@param: dimensao, numero de neuronio (matriz quadrada), conjunto de treino e seus rotulo, conj de teste e seus rotulos
n = Map(1024,header[0],Xtr,ytr,Xte,yte)

#Cria outra instancia
n1 = Map(1024,header2[0],Xtr,ytr,Xte,yte)

#Funcao que carrega os pesos de uma rede
#@param: o vetor de pesos da rede a ser carregada
n.loadNetwork(weights,labels)

#Chama a mesma funcao para outra instancia
n1.loadNetwork(weights2,labels2)

#Classifica a rede em relacao ao conjunto de teste
#@param: cabecalho contendo as informacoes sobre a rede, tais como: numero de neuronios e erro originario
n.classify(header)

#Classifica para a outra instancia
n1.classify(header2)

#Chama a funcao que mostra o grafico na tela
plt.show()