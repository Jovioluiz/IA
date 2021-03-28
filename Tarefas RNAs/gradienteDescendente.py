# TAREFA 3

#cálculo do gradiente

import numpy as np

#função sigmoide
def sigmoid(x):
    return 1/(1 + np.exp(-x))

#derivada da função sigmoide
def sigmoid_prime(x):
    return sigmoid(x) * (1-sigmoid(x))

#taxa de aprendizado
learnrate = 0.5

x = np.array([1, 2, 3, 4])
y = np.array([0.5])
bies = 0.5

#pesos iniciais
w = np.array([0.5, -0.5, 0.3, 0.1])

#calculo da combinação linear de entrada dos pesos do nó
h = np.dot(x, w) + bies

nn_output = sigmoid(h)
print('Output da rede inicial: {}' .format(nn_output))

#erro calcular de rede neural
error = y - nn_output
print('Erro Inicial: {}'.format(error))

#calcular termo do erro
erro_term = error * sigmoid_prime(h)
print('Termo de erros inicial: {}'.format(erro_term))

print('Peso Inicial: {}'.format(w) + '\n')

#calcule a mudança nos pesos
del_w = learnrate * erro_term * x

#aplicando os novos pesos
w = w + del_w

h = np.dot(x, w) + bies
nn_output = sigmoid(h)

#erro calcular de rede neural
error = y - nn_output

#calcular termo do erro
erro_term = error * sigmoid_prime(h)

#atualizando o passo
del_w = learnrate * erro_term * x

#aplicando os novos pesos
w = w + del_w

print('Output da rede: {}' .format(nn_output))
print('Erro do Output: {}'.format(error))
print('Termo de erro: {}'.format(erro_term))
print('Novos Pesos: {}' .format(w))
print('Passos: {}' .format(del_w))