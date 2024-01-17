import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

df = pd.read_csv('../datasets/elections-presidentielles2022-1ertour.csv', delimiter=';')

# removing useless columns
df = df.drop(
    columns=['type_election', 'annee', 'numero_tour', 'date_tour', 'circ_bv', 'quartier_bv', 'sec_bv', 'num_bureau','id_bvote','geo_shape','geo_point_2d']
)

# grouping vote results by arr_bv
grouped_by_arr_bv = df.groupby(['arr_bv']).sum()

grouped_by_arr_bv['extreme_gauche'] = grouped_by_arr_bv[['arthaud_nathalie', 'roussel_fabien', 'melenchon_jean_luc','poutou_philippe']].sum(axis=1)
grouped_by_arr_bv['gauche'] = grouped_by_arr_bv[['hidalgo_anne']].sum(axis=1)
grouped_by_arr_bv['centre'] = grouped_by_arr_bv[['lassalle_jean']].sum(axis=1)
grouped_by_arr_bv['droite'] = grouped_by_arr_bv[['macron_emmanuel','pecresse_valerie']].sum(axis=1)
grouped_by_arr_bv['extreme_droite'] = grouped_by_arr_bv[['le_pen_marine','zemmour_eric','dupont_aignan_nicolas']].sum(axis=1)
grouped_by_arr_bv['ecologie'] = grouped_by_arr_bv[['jadot_yannick']].sum(axis=1)

# profile = ProfileReport(grouped_by_arr_bv, title='Election Profiling')
# profile.to_file(output_file='profiling_report.html')

grouped_by_arr_bv.to_csv('transformed_df.csv', sep=';')
