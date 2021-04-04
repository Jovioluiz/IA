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
y = np.array([0.5])#valor esperado
bies = 0.5

#pesos iniciais
w = np.random.randn(4)/10

epocas = 100

del_w = 0

for e in range(epocas):
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

    print('Saída da rede: {}' .format(nn_output))
    print('Erro: {}'.format(error))
    if nn_output == 0.5:
        break