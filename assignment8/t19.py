def find_elements_with_substring(lst, substring):
     return list(filter(lambda x: substring in x, lst))
 
 original_list = ['red', 'black', 'white', 'green', 'orange']
 substring1 = "ack"
 result1 = find_elements_with_substring(original_list, substring1)
 print("Elements of the list that contain substring '{}':".format(substring1), result1)
 
 substring2 = "abc"
 result2 = find_elements_with_substring(original_list, substring2)
 print("Elements of the list that contain substring '{}':".format(substring2), result2)