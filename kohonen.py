import numpy as np
from mvpa2.suite import *
tam = 1934
# esta funcao le o arquivo original e transforma em um vetor numpy
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
		
	return arr
	
arq = readFile('optdigits1.data')
X = arq[:,:1024]
y = arq[:,1024]
# esta funcao le o arquivo original e transforma em um vetor numpy


#so = SimpleSOMMapper#((10,10),200,learning_rate= 0.01)
#so.train(X)



