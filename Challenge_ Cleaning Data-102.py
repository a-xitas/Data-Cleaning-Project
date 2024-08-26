## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

#avengers['Year'].hist()


true_avengers = avengers[avengers['Year'] >=  1960].copy()

avengers['Year'].hist()

## 5. Consolidating Deaths ##

print(true_avengers.columns)

# Primeiro transformar os NaN's em 0 recorrendo ao método fillna():
true_avengers[['Death1', 'Death2', 'Death3', 'Death4', 'Death5', 'Return1', 'Return2', 'Return3', 'Return4',
               'Return5']] = true_avengers[['Death1', 'Death2', 'Death3', 'Death4', 'Death5', 'Return1', 'Return2', 'Return3', 'Return4',
               'Return5']].fillna(0).copy()

# De seguida criar uma lista com as cols que queremos usar para calcular o nmr de mortes. Q deverá dizer respeito a todas as colunas que incluam mortes (Deaths):
deaths = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']

# Por último, identificar todas as colunas anteiriores que digam 'YES' ou seja, que digam q sim, q um Avenger morreu, e somar, linha a linha (axis=1), esse nmr de YES's. Atribuir depois esse somatório a uma nova coluna de nome 'Deaths':
true_avengers['Deaths'] = (true_avengers[deaths] == 'YES').sum(axis=1).copy()
    




## 6. Verifying Years Since Joining ##

# Primeiro vamos tentar calcular a diferença entre os anos em que os Avengers entraram pela 1º vez, e o ano de analise, 2015. Isto para conseguirmos perceber à qtos anos está cada personagem na serie:
joined_years  = (2015 - true_avengers['Year']).astype(int)

# De seguida vamos ver qtos desses anos calculados por Nós manualmente, são iguais aos anos que estão no Dataset, na col 'Years since joining':
joined_Vs_Years = joined_years == true_avengers['Years since joining']

# Por último vamos contar esse nmr e atribuilo à variável joined_accuracy_count:
joined_accuracy_count = len(joined_Vs_Years)