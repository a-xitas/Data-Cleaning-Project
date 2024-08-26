## 3. Finding Correlations With the r Value ##

# vamos, agora que limpamos o N/Dataset de todos os NAN's, sacar as correlações para todas as colunas do Dataset 'combined', usando o método corr():

correlations = combined.corr()

correlations = correlations['sat_score'].copy()

print(correlations['total_enrollment'])


## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(x=combined['total_enrollment'], y=combined['sat_score'], c='red', alpha=0.8)
ax.set_xlabel('total_enrollment')
ax.set_ylabel('sat_score')

plt.show()



## 6. Exploring Schools with Low SAT Scores and Enrollment ##


low_enrollment = combined[(combined['sat_score'] < 1000) & (combined['total_enrollment'] < 1000)].copy()

school = low_enrollment['SCHOOL NAME']

print(school)

## 7. Plotting Language Learning Percentage ##

fig, ax = plt.subplots()


plt.scatter(x=combined['ell_percent'], y=combined['sat_score'], c='red', alpha=0.5, s=20)
ax.set_xlabel('ell_percent')
ax.set_ylabel('sat_score')

plt.show()

## 8. Calculating District-Level Statistics ##

# o gráfico anteriormente gerado é mt pco perceptível. Isto pq os plots estão a ser gerados e plotados com base na distribuição original, a q está no DataSet combined, q estão tds dispostos de forma aleatória.
import numpy as np

# o que vamos fazer agora é agrupar (groupby()) o N/Dataset combined pelo distrito de cada escola ('school_dist') e sacar as médias das outras colunas todas(agg(np.mean)). Isto para quê, para ao plotarmos, plotarmos a info por distrito. Assim, ao inves de ter por exemplo 30 prontos em cima de Bronx, e n se conseguir perceber nada, temos apenas 1 ponto q corresponderá à média de todos os elementos que compõe o distrito de Bronx. Tornando dessa forma o N/mapa mt mais limpo e fácil de visualizar:
districts = combined.groupby(combined['school_dist']).agg(np.mean).reset_index().copy()

districts.head()