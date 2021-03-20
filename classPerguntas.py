from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['O animal está agitado?','agitado'],
		['O animal está comendo bem?','alimentado'],
		['O ambiente é adequado?','ambiente_adequado'],
		['O animal está calmo?','calmo'],
		['O animal está com febre ou tosse?', 'doente'],
		['O animal está se movimentando bem?', 'n_movimenta']
		]

	def texto(self):
		if len(self.level) <= 6:
			string = self.level[0]
			del self.level[0]
			return string
