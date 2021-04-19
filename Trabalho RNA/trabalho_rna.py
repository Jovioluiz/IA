import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Função do cáculo da sigmóide
def sigmoid(x):
    return 1/(1+np.exp(-x))

#deriva da função sigmoide
def sigmoid_prime(sigmoid_):
    return sigmoid_ * (1 - sigmoid_)

def calc_combinacao_linear (i, w):
    inputs = np.array(i)
    weights = np.array(w)
    return np.dot(inputs, weights)

DataSet=pd.read_csv('arruela_.csv')

DataSet.head()

DataSet.drop(['Hora','Tamanho'], axis=1, inplace=True)

DataSet.head()

DataSet.describe()

DataSet.columns

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
DataScaled = scaler.fit_transform(DataSet)
DataSetScaled = pd.DataFrame(np.array(DataScaled), columns = ['Referencia','NumAmostra', 'Area', 'Delta', 'Output1','Output2'])

DataSetScaled.head()

x = DataSetScaled.drop(['Output1', 'Output2'], axis=1)
y = DataSet[['Output1','Output2']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=101)


#Tamanho do DataSet de Treinamento
n_records, n_features = X_train.shape

#Arquitetura da MPL
N_input = 4
N_hidden = 3
N_output = 2
taxa_aprendizagem = 0.3

#Pesos da Camada Oculta (Inicialização Aleatória)
pesos_ent_camada_oculta = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
#Pesos da Camada de Saída (Inicialização Aleatória)
pesos_camada_saida = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))

epocas = 3000
last_loss = None
EvolucaoError = []
IndiceError = []

for e in range(epocas):
    delta_pesos_camada_oculta = np.zeros(pesos_ent_camada_oculta.shape)
    delta_pesos_camada_saida = np.zeros(pesos_camada_saida.shape)

    for entrada, yi in zip(X_train.values, y_train.values):
        # Forward Pass
        # Calculo das saidas
        saida_oculta = sigmoid(calc_combinacao_linear(entrada, pesos_ent_camada_oculta))
        saida_camada_oculta = sigmoid(calc_combinacao_linear(saida_oculta, pesos_camada_saida))

        erro = yi - saida_camada_oculta

        gradiente_saida = erro * sigmoid_prime(saida_camada_oculta)

        erros_ocultos = calc_combinacao_linear(pesos_camada_saida, gradiente_saida)
        gradiente_saida_oculta = erros_ocultos * sigmoid_prime(saida_oculta)


        #Calculo da variação do peso da camada de saída
        delta_pesos_camada_oculta += gradiente_saida_oculta * entrada[:, None]

        #Calculo da variação do peso da camada oculta
        delta_pesos_camada_saida += gradiente_saida * saida_oculta[:, None]

    # Atualização dos pesos na época em questão
    pesos_ent_camada_oculta += taxa_aprendizagem * delta_pesos_camada_oculta / n_records
    pesos_camada_saida += taxa_aprendizagem * delta_pesos_camada_saida / n_records

    # Imprime o erro quadrático médio no conjunto de treinamento
    if e % (epocas / 20) == 0:
        saida_oculta = sigmoid(np.dot(entrada, pesos_ent_camada_oculta))
        out = sigmoid(calc_combinacao_linear(saida_oculta, pesos_camada_saida))
        loss = np.mean((out - yi) ** 2)

        if last_loss and last_loss < loss:
            print("Erro quadrático no treinamento: {}".format(loss), " Atenção: O erro está aumentando")
        else:
            print("Erro quadrático no treinamento: {}".format(loss))
        last_loss = loss

        EvolucaoError.append(loss)
        IndiceError.append(e)

plt.plot(IndiceError, EvolucaoError, 'r')  # 'r' is the color red
plt.xlabel('Número de Épocas')
plt.ylabel('Erro Quadrático')
plt.title('Evolução do Erro no treinamento da MPL')
plt.show()

# Calculo da precisão dos dados de teste
n_records, n_features = X_test.shape
predictions = 0

for xi, yi in zip(X_test.values, y_test.values):

    # Forward Pass
    saida_oculta = sigmoid(calc_combinacao_linear(xi, pesos_ent_camada_oculta))
    output = sigmoid(calc_combinacao_linear(saida_oculta, pesos_camada_saida))

    # Cálculo do Erro da Predição
    if (output[0] > output[1]):
        if (yi[0] > yi[1]):
            predictions += 1

    if (output[1] >= output[0]):
        if (yi[1] > yi[0]):
            predictions += 1

print("A Acurácia da Predição é de: {:.3f}".format(predictions / n_records))