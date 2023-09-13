import pandas as pd
import numpy as np
import string

from od_data_preprocessing import try_indexing

# trip_data = pd.read_pickle('pickles/tm_trip_data1.pkl')
# print(trip_data)

"""## Loading Nodes DataFrame"""

def load_and_print(filename):
    loaded_df = pd.read_pickle(filename)
    return loaded_df

nodes_df = load_and_print('pickles/tokyo_metro_nodes.pkl')
nodes = list(nodes_df['station_name'])

"""Correct station names"""

def correct_station(name):
    return nodes[try_indexing(name)]

# trip_data['enter_station_name'] = trip_data['enter_station_name'].apply(correct_station)
# trip_data['exit_station_name'] = trip_data['exit_station_name'].apply(correct_station)

# print(trip_data)
# trip_data.to_pickle(f'pickles/tm_trip_data.pkl')

trip_data = pd.read_pickle('pickles/tm_trip_data.pkl')
print(trip_data)

MATRIX_SIZE = len(nodes)
print(MATRIX_SIZE)

TIMESTEPS = 24

matrix_list = [np.zeros((MATRIX_SIZE, MATRIX_SIZE)) for _ in range(TIMESTEPS)]
# Starts from 0 = 12:00am to 23 = 23:00pm

for _, row in trip_data.iterrows():
    enter_time = row['enter_time'] % 24
    origin = nodes.index(row['enter_station_name'])
    dest   = nodes.index(row['exit_station_name'])

    if origin and dest:
        matrix_list[enter_time][origin, dest] += row['num_people']

print(matrix_list)

np.savez('matrix_list_144x144.npz', *matrix_list)
