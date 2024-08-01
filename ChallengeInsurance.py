import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import TrainningModel
from sklearn.preprocessing import LabelEncoder


# Lendo o arquivo de dados
dados = pd.read_csv(".venv/database/insurance.csv")
print(dados.head())

#Verificando se temos dados nulos no arquivo de insurance
msno.matrix(dados)
print(dados.isnull().sum())

#pré processamento de variáveis
encoder = LabelEncoder()
dados['gender'] = encoder.fit_transform(dados['sex'])

dummy_dados = pd.get_dummies(dados, columns=["sex"])
#print(dummy_dados.head())


# Visualizando em gráfico, idade por cobranças
dados.plot.scatter(x="age", y="charges")
plt.show()

# Treinamento
TrainningModel.trainModel(dados, plt)





