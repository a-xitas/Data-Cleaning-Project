## 3. Condensing the Class Size Dataset ##


class_size = data['class_size']

class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']

class_size.head()

## 5. Computing Average Class Sizes ##

import numpy as np

class_size = class_size.groupby('DBN').agg(np.mean).copy()
9
class_size.reset_index(inplace=True)

data['class_size'] = class_size.copy()

data['class_size'].head()

## 7. Condensing the Demographics Dataset ##

demographics = data['demographics']

demographics = demographics[demographics['schoolyear']==20112012]

demographics.head()

data['demographics'] = demographics.copy()

data['demographics'].head()


## 9. Condensing the Graduation Dataset ##

graduation = data['graduation']

graduation = graduation[(graduation['Cohort'] == '2006') & (graduation['Demographic'] == 'Total Cohort')]

data['graduation'] = graduation.copy()

data['graduation'].head()
                        
                        

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

ap_2010 = data['ap_2010']

for c in cols:
    data['ap_2010'][c] = pd.to_numeric(data['ap_2010'][c], errors='coerce')
    
    
print(data['ap_2010'].dtypes)

#data['ap_2010']['AP Test Takers '].head()
    

## 12. Performing the Left Joins ##

combined = data["sat_results"]

combined = combined.merge(data['ap_2010'], on='DBN', how='left').copy()

combined = combined.merge(data['graduation'], on='DBN', how='left').copy()

combined.head()
combined.shape
                    

## 13. Performing the Inner Joins ##

ds = ['class_size', 'demographics', 'survey', 'hs_directory']

for s in ds:
    combined = combined.merge(data[s], how='inner', on='DBN').copy()


combined.head()
combined.shape



## 15. Filling in Missing Values ##

means = combined.mean()

combined = combined.fillna(means).copy()

#contar o nmr de NaN's num DataSet, usando o metódo isna() combinado com a soma dos valores que são NaN's (sum()):
combined.isna().sum()

# como ainda temos NAN's presentes no Nosso DataSet 'combined' e n podemos, pq p sacarmos uma correlação temos q ter 0 NAN's, vamos ter que preencher os restantes NaN's com o valor 0

combined = combined.fillna(0).copy()
# o motivo pelo qual existem NaN's e q n foram mitigados em algumas colunas é pq nessas colunas poderia n exister quaisquers valores para além dos NaN's que nos permitisse calcular uma média e atribui-la aos valores em falta! Como poderemos sacar uma média de uma coluna que está ela toda povoada com NaN's apenas? IMPOSSÍVEL! 
combined.isna().sum()

combined.head()

print(combined.columns)

## 16. Adding a School District Column for Mapping ##

def ext(DBN):
    district = DBN[0:2]
    return district


combined['school_dist'] = combined['DBN'].apply(ext).copy()

combined['school_dist'].head()
