# tarefa 6
# Jóvio L. Giacomolli
import math

import pandas as pd
import numpy as np


# função sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


dataset = pd.read_csv('Data.csv')
dataset.head()
dataset.columns

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(dataset.drop(['Output1', 'Output2'], axis=1),
                                                    dataset[['Output1', 'Output2']], test_size=0.33,
                                                    random_state=101)

n_records, n_features = x_train.shape

# Arquitetura da MPL
n_input = 3
n_hidden = 4
n_output = 2
learnrate = 0.5

# vetor dos valores de entrada(aleatoria)
# x = np.array([1, 2, 3])
# target = 0.6
# learnrate = 0.5

# pesos camada oculta

weights_input_hidden = np.random.normal(0, scale=0.1, size=(n_input, n_hidden))
print('Peso da entrada oculta: {}'.format(weights_input_hidden))

# pesos camada de saida
weights_hidden_output = np.random.normal(0, scale=0.1, size=(n_hidden, n_output))
print('Peso da camada de saída: {}'.format(weights_hidden_output))

epocas = 5000
last_loss = None
evolucaoErro = []
indiceErro = []

for i in range(epocas):
    delta_w_i_h = np.zeros(weights_input_hidden.shape)
    delta_w_h_o = np.zeros(weights_hidden_output.shape)

    for xi, yi in zip(x_train.values, y_train.values):

        # forward pass

        # camada oculta
        # calcule a combinação linear de entradas e pesos sinápticos
        hidden_layer_input = np.dot(xi, weights_input_hidden)
        hidden_layer_output = sigmoid(hidden_layer_input)

        # camada de saida

        output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)

        # aplicar a função de ativação
        output = sigmoid(output_layer_in)

        # print('As saidas da rede são: {}'.format(output))

        # backward pass

        error = yi - output
        # calculo do termo do erro
        output_error_term = error * output * (1 - output)

        hidden_error = np.dot(weights_hidden_output, output_error_term)

        hidden_error_term = hidden_error * hidden_layer_output * (1 - hidden_layer_output)

        delta_w_h_o += learnrate * output_error_term * hidden_layer_output[:, None]
        # print(delta_w_h_o)
        # print('\n')
        delta_w_i_h += learnrate * hidden_error_term * xi[:, None]
        # print(delta_w_i_h)
        # print('\n')
        weights_input_hidden += learnrate * delta_w_i_h / n_records

        # print('\n')
        weights_hidden_output += learnrate * delta_w_h_o / n_records

        if i % (epocas / 20) == 0:
            hidden_output = sigmoid(np.dot(xi, weights_input_hidden))
            out = sigmoid(np.dot(hidden_output, weights_hidden_output))
            loss = np.mean((out - yi) ** 2)

            if last_loss and last_loss < loss:
                print("Erro quadrático no treinamento: ", loss, " Atenção: O erro está aumentando")
            else:
                print("Erro quadrático no treinamento: ", loss)
            last_loss = loss

            evolucaoErro.append(loss)
            indiceErro.append(i)

# Calcule a precisão dos dados de teste
n_records, n_features = x_test.shape
MSE_Output1 = 0
MSE_Output2 = 0
RMSE_Output1 = 0
RMSE_Output2 = 0

for xi, yi in zip(x_test.values, y_test.values):
    # Forward Pass
    # Camada oculta
    # Calcule a combinação linear de entradas e pesos sinápticos
    hidden_layer_input = np.dot(xi, weights_input_hidden)
    # Aplicado a função de ativação
    hidden_layer_output = sigmoid(hidden_layer_input)

    # Camada de Saída
    # Calcule a combinação linear de entradas e pesos sinápticos
    output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)

    # Aplicado a função de ativação
    output = sigmoid(output_layer_in)

    # Cálculo do Erro
    #TODO: Cálculo do Erro
    error = yi - output
    MSE_Output1 += (yi[0] - output[0]) ** 2
    MSE_Output2 += (yi[1] - output[1]) ** 2

# Erro Quadrático Médio
MSE_Output1 /= n_records
MSE_Output2 /= n_records

RMSE_Output1 = math.sqrt(MSE_Output1)
RMSE_Output2 = math.sqrt(MSE_Output2)

print('Erro Quadrático Médio da Saída Output1 é: ', MSE_Output1)
print('Erro Quadrático Médio da Saída Output2 é: ', MSE_Output2)

print('Raiz do Erro Quadrático Médio da Saída Output1 é: ', RMSE_Output1)
print('Raiz do Erro Quadrático Médio da Saída Output2 é: ', RMSE_Output2)