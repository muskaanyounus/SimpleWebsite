Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]

original_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = []
for sublist in original_list:
    if sublist not in new_list:
        new_list.append(sublist)
print("New List:", new_list)
