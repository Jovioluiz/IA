#TAREFA 2
#cálculo do gradiente

import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))


def sigmoid_prime(x):
    #derivada da função sigmoide
    return sigmoid(x) * (1-sigmoid(x))

#taxa de aprendizado
learnrate = 0.5

x = np.array([1,2,3,4])
y = np.array([0.5])
bies = 0.5

#pesos iniciais
w= np.array([0.5, -0.5, 0.3, 0.1])

h = np.dot(x, w) + bies

nn_output = sigmoid(h)
print(nn_output)
#erro calcular de rede neural
error = y - nn_output

#calcular tsermo do erro
erro_term = error * sigmoid_prime(h)

#calcule a mudança nos pesos
del_w = learnrate * erro_term * x
print(del_w)

#aplicando os novos pesos
w = w + del_w
print(w)

h = np.dot(x, w) + bies
nn_output = sigmoid(h)
print(nn_output)