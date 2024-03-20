

from itertools import chain

int_array = [[1,2,3], [4,5,6], [7,8,9]]

def flatten_list(int_array):
    return list(chain.from_iterable(int_array))


flattened_array = flatten_list(int_array)
print(flattened_array)

# this is extra code, I wanted to find out how can I print the outcome in decending order. 
print(sorted(flattened_array, reverse=True))
