#from classDiagnostico import *
#from classPerguntas import *

#Inferência
from classPerguntas import *
from classDiagnostico import *

se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0], string[1])
	print('probabilidade é %d' %(se.probabilidade()) + '\n')
	print(se.resultado)
	if se.probabilidade() == 100:
		print('O suino está: ', se.resultado[0] + '\n')