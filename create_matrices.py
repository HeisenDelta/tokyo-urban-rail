import pandas as pd
import numpy as np


"""Requirements"""

def load_and_print(filename):
    loaded_df = pd.read_pickle(filename)
    return loaded_df

def ingest_matrix_list(filename):
    matrix_list = np.load(filename)
    return [matrix_list[f'arr_{i}'] for i in range(24)]

nodes_df = load_and_print('pickles/tokyo_metro_nodes.pkl')
nodes = list(nodes_df['station_name'])

matrix_list = ingest_matrix_list('matrix_list_144x144.npz')

"""Creating the Matrix"""

skip_station = ['Wakoshi', 'Nishi-funabashi', 'Nakano', 'Naka-meguro', 'Meguro', 'Yoyogi-uehara']
to_remove = list(map(lambda x: nodes.index(x), skip_station))

matrix_list_138 = []

for matrix_144 in matrix_list:
    indices_to_keep = np.delete(np.arange(144), to_remove)

    matrix_138 = matrix_144[indices_to_keep][:, indices_to_keep]
    matrix_list_138.append(matrix_138)

np.savez('matrix_list_138x138.npz', *matrix_list_138)
