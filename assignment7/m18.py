Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False

list1 = [{},{},{}]
list2 = [{1,2},{},{}]  
list2 = [{'a': 1}, {}, {}]
def all_dicts_empty(lst):
    return all(len(d) == 0 for d in lst)

print(all_dicts_empty(list1))  
print(all_dicts_empty(list2)) 
