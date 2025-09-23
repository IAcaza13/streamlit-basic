import pandas as pd
import numpy as np

data = {
    'Alumne': ['Anna', 'Bernat', 'Carla', 'David', 'Wally', 'Xavi', 'Yaiza', 'Zulema'],
    'Examen1': [7, 4, 10, 6, 5, 6, 10, 7],
    'Examen2': [6, 8, 7, 9, 3, 8, 7, 8],
    'Examen3': [8, 7, 9, 8, 6, 7, 8, 10]
}
df1 = pd.DataFrame(data)

#El teu codi va aquí
print(df1['Examen2'].describe())
print(df1['Yaiza'])
print(df1['Anna'])
IQR = df1['Examen1'].quantile(0.75) - df1['Examen1'].quantile(0.25)
print(IQR)


# Tests
assert IQR == 2, "Error: IQR incorrecte."
assert df1['Final'].iloc[0] == 7, "Error: Nota Final incorrecte per Anna."
assert round(mean_final, 2) == 7.25, "Error: Mitjana incorrecta."
assert round(std_final, 2) == 1.32, "Error: Desviació típica incorrecta."