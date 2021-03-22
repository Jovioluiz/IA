from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Possui algum LED desligado?', 'ledDesligado'],
		['O processo foi inicializado?', 'iniciadoProcesso'],
		['Suga água do reservatório no inicio do processo?', 'sugaAgua'],
		['O fluxo de água dentro dos canos e mangueiras está normal?', 'fluxoAgua'],
		['Realiza o processo completo?', 'realizaProcessoCompleto'],
		['Recepiente está aquecendo?','estaAquecendo'],
		['Sensores de temperatura e pressão estão funcionando corretamente?', 'sensoresNaofunciona']
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
