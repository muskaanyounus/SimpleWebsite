my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
unique_dict = {}
for k, v in my_dict.items():
if v not in unique_dict.values():
unique_dict[k] = v
print(unique_dict)
