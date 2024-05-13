import numpy as np

dict = {'India': 'Delhi', 'Cuba': 'Havana','Egypt': 'Cario', 'Nepal': 'Kathmandu'}
print(dict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value}

print(sorted_dict)
