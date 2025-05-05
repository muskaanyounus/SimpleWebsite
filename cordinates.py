def convert_to_positive_coordinates(coordinates):
     min_x = min(coordinates, key=lambda x: x[0])[0]
     min_y = min(coordinates, key=lambda x: x[1])[1]
 
     shift_x = abs(min_x)
     shift_y = abs(min_y)
 
     shifted_coordinates = [(x + shift_x, y + shift_y) for x, y in coordinates]
 
     return shifted_coordinates
 
 
 coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
 output = convert_to_positive_coordinates(coordinates)
 print(output)