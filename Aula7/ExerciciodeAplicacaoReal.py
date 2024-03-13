import pandas as pd

igm_df = pd.read_csv('Aula7/igm_modificado.csv')


ind_des = igm_df['indice_governanca']
print(ind_des)