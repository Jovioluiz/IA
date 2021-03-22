class Diagnostico():
	# metodo construtor
	def __init__(self):
		self.resultado = ['LEDQueimado',
						  'fonteQueimada',
						  'trocarSensoresDefeituosos',
						  'trocarDisplay',
						  'trocarPainel',
						  'trocarPlaca',
						  'trocarResistencia',
						  'problemaBombaAgua',
						  'sujeiraMangueiraseCanos']
		self.db = []
		# abre o arquivo database.txt em modo leitura e passa os dados para
		# uma lista de listas de str
		arquivo = open('database.txt','r')
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
	def busca(self, problema, caract):
		for i in range(len(self.db)):
			if problema == self.db[i][1]:
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

	# Mantêm um parâmetro no resultado idependente da resposta da pergunta
	def excessao(self, atributo):
		self.resultado.append(atributo)
		
	def pergunta(self, pergunta, caract):
		resp = input(pergunta + ': ')
		if resp.upper() == 'S':
			self.excluiquemnaoe(caract)	
		elif resp.upper() == 'N':
			self.excluiqueme(caract)
		elif resp == '':
			raise Exception("Informe uma resposta!")
		else:
			raise Exception("Resposta errada! Informe S para sim e N para não.")

	#Pergunta que possui o parametro com excessão		
		if pergunta == 'Suga água do reservatório no inicio do processo?' and resp.upper() == 'S':
			self.excessao('sujeiraMangueiraseCanos')