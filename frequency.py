import numpy as np
import pandas as pd

data = "6 7 2 5 7 3 4 1 12 9 2 7 1 6 5 8 9 11 6 2 5 4 6 8 13 12 8 4 6 5 7 9 7 10 5 6 2 7 7 4"
data = data.split(" ")
data = [int(i) for i in data]
data_length = len(data)

index_bounds = [(1,3),(4,6),(7,9),(10,12),(13,15)]
index_frequencies = []
for i in index_bounds:
    index_frequencies.append([])

for datum in data:
    for bounds in index_bounds:
        if datum >= min(bounds) and datum <= max(bounds):
            index_frequencies[index_bounds.index(bounds)].append(datum)

data_array = np.array([np.array(i) for i in index_frequencies], dtype=object)
data_arrays = []

for i in range(len(data_array)):
    data_array[i] = len(data_array[i])
for i in range(len(data_array)):
    data_array[i] = [data_array[i], data_array[i]/data_length, data_array[i]/data_length*100]
    data_arrays.append(data_array[i])

frequency_data_frame = pd.DataFrame(data = data_arrays, index = index_bounds, columns = ['frequency', 'relative frequency','%'])
print(frequency_data_frame)

