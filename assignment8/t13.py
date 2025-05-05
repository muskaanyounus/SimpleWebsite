phones = [
     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
 ]
 
 sorted_phones = sorted(phones, key=lambda x: int(x['model']))
 
 print("Sorted list of dictionaries:", sorted_phones)