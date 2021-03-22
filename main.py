#from classDiagnostico import *
#from classPerguntas import *

#Inferência
from trunk.classDiagnostico import *
from trunk.classPerguntas import *

se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0], string[1])
	print('probabilidade é {}%' .format(se.probabilidade()) + '\n')
	print(se.resultado)
	if se.probabilidade() == 100:
		print('O problema é: {} ' .format(se.resultado[0]) + '\n')