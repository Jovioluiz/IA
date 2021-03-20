class Diagnostico():
	# metodo construtor
	def __init__(self):
		self.resultado = ['estressado', 'faminto', 'saudavel','com_calor','cansado','machucado','bem_alimentado','com_frio','deprimido','nao_movimenta',
						  'tosse','febre', 'dificuldade_respirar']
		self.animal = []
		self.db = []
		# abre o arquivo db2.txt em modo leitura e passa os dados para
		# uma lista de listas de str
		arquivo = open('db_dois.txt','r')
		for linha in arquivo:
			if linha[len(linha) - 1] == '\n':
				linha = linha.replace("\n", "")
				(self.db).append(linha.split('-'))
		arquivo.close()

	# imprime a quantidade de possibilidades cadastradas
	def tamanho(self):
		print(len(self.resultado))

	# imprime a probabilidade do diagnótico
	def probabilidade(self):
		try:
			return (int((1 / int(len(self.resultado))) * 100))
		except ZeroDivisionError:
			return 0

	# verifica se diagnóstico pensado tem a caracteristica passada por parametro
	def busca(self, familiar, caract):	
		for i in range(len(self.db)):
			if familiar == self.db[i][1]:
				if self.db[i][0] == caract:
					return True
		return False				

	# remove os diagnósticos que não possuem o atributo passado por parametro
	def excluiquemnaoe(self, atributo):
		lista = []
		count = 0
		for i in range(len(self.resultado)):
			if not self.busca(self.resultado[i], atributo):
				lista.append(self.resultado[i])
				count = count + 1
		for i in range(count):
			self.resultado.remove(lista[i])
	
	# remove os diagnosticos que possuem o atributo passado por parametro
	def excluiqueme(self, atributo):
		lista = []
		count = 0
		for i in range(len(self.resultado)):
			if self.busca(self.resultado[i], atributo):
				lista.append(self.resultado[i])
				count = count + 1
		for i in range(count):
			self.resultado.remove(lista[i])
		
	def pergunta(self,pergunta,caract):
		resp = input(pergunta + ': ')
		if resp.upper() == 'S':
			self.excluiquemnaoe(caract)
		elif resp.upper() == 'N':
			self.excluiqueme(caract)

"""
'O animal está agitado?'			->		'agitado'
'O animal está comendo bem?'		->		'alimentado'
'O animal está calmo?'				->		'calmo'
'O ambiente é adequado?'			->	'ambiente_adequado'
'O animal não se alimentou?' 		-> 	'doente'
'O animal está com tosse?'			->	'doente'
'O animal está com febre?'			->	'doente'
'O animal está com dificuldade respirar?'	->	'doente'
'O animal não está se movimentando?'	->	'n_movimenta'

"""