#RNA de um neuronio

import numpy as np

#função de calculo sigmóide
def sigmoid(x):
    return 1/(1+np.exp(-x))

#vetor de entrada
x = np.array([0.8,-0.3])
b = 0.1

#ligação sinaptica
w = np.array([0.2,-0.1])

#calcula a combinação linear de entradas e pesos sinápticos
h = np.dot(x, w) + b

y = sigmoid(h)

print('a saída da rede é ', y)