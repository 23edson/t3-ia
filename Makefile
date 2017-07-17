#   Universidade Federal da Fronteira Sul
# 
#                TRABALHO III
#   
#   Disciplina: Inteligência Artificial
#   Professor: José Carlos Bins Filho
#    
#   Aplicação: rede de Kohonen para reconhecimento de dígitos. 
# 	
#
#   Alunos : Edson Lemes da Silva && Lucas Cezar Parnoff
#
#
#  --- MAKEFILE DE EXECUÇÃO ---

train: treina.py
	python treina.py

test: testa.py
	python testa.py
