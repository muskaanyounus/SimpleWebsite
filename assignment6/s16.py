# 16
print("\n16. List input and deletion:")
my_list = input("Enter list elements separated by space: ").split()
to_delete = input("Enter element to delete: ")
if to_delete in my_list:
    my_list.remove(to_delete)
print("Updated list:")
for item in my_list:
    print(item)