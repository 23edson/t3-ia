	Universidade Federal da Fronteira Sul.
 
	TRABALHO III
   
	Disciplina: Inteligência Artificial;
	Professor: José Carlos Bins Filho;
    
	Aplicação : rede de Kohonen para reconhecer dígitos ;
 	

	Alunos : Edson Lemes da Silva && Lucas Cezar Parnoff.
	
**Descrição Geral**

Esta aplicação recebe lê o arquivo 'optdigits.data', separa entre conjunto de treino
e teste com 70% e 30% respectivamente. Após isto, faz o treinamento via rede de Kohonen,
classifica e apresenta o resultado. Os componentes deste trabalho estão descritos com maiores 
detalhes no arquivo relatorio.pdf.


**1.Execução**

Este algoritmo foi executado utilizando o Python 2.7, no Linux. Alguns pacotes são
necessários para a execução correta, a forma de instalação são:

pip intall numpy
sudo apt-get install python-matplotlib

Essa instalação se da através de um terminal no Linux.

A implementação do algoritmo de Kohohen encontra-se no arquivo 'som.py';
O arquivo 'readFile.py' apresenta funções de leitura;
Como forma de exemplos: há dois arquivo, chamados de 'treina.py' e 'testa.py',
o primeiro realiza a execução do algoritmo e treina uma rede. E o segundo arquivo,
executa o carregamento de uma rede em disco, e executa a classificação.

Para simplificação, estes programas podem ser executados via Makefile,

Opções do Makefile:
	Make train
	Make test
A primeira opção executa o arquivo 'treina.py' e o segundo 'testa.py'.

Alternativamente, pode ser executado diretamente do interpretador Python,
para isto, pode-se seguir os seguintes passos:
Em um terminal Linux (aberto no diretório do projeto)
	python
	execfile("treina.py")
	ou execfile("testa.py")
Assumindo que a versão aberta é Python2, ou alguma anterior ao Python3, por
questões de compatibilidade.

Há dois arquivos com redes treinadas, são eles: 'rtreinada.data' e 'rtreinada1.data'. As
primeira com 36 neurônios e a segunda com 16 neurônios. Cada um deles possui um arquivo semelhante 
nomeados de 'lrtreinada' e 'lrtreinada1.data' que representam os rótulos para cada
neurônio.

Outros detalhes como: tratamento da base de dados, algoritmo de Kohonen e classificação estão descritos
no arquivo relatorio.pdf.
	
