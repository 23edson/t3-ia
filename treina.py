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
*   Este é um arquivo exemplo de como treinar uma rede.
*   Deste modo, é feito a leitura do conjunto de dados, a
*   separação entre conjunto de treino e teste, treinamento
*   e finalmente a classificação e salvamento da rede.

'''

from som import *

#Carrega o conjunto original de dados
conj = readFile("optdigits.data")

#Divide o conjunto em treino e teste com seus rotulos
Xtr,ytr,Xte,yte = divideSet(conj)

#Cria uma instancia da classe Map
#@param: dimensao, numero de neuronio (matriz quadrada), conjunto de treino e seus rotulo, conj de teste e seus rotulos
n = Map(1024,4,Xtr,ytr,Xte,yte)

#Funcao que treina a rede
#@param: condicao de parada (erro em relacao a atualizacao dos pesos), flag para debug(True ou False) 
n.train(0.01,True)

#Classifica a rede em relacao ao conjunto de teste
#@param: None significado que nao precisa de nenhum metadados de arquivo externo, pois a rede ja esta na memoria
n.classify(None)

#Salva a rede no arquivo "rtreinada4.data"
#@param: nome e caminho do arquivo
n.saveNetwork("rtreinada4.data")