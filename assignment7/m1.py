data = {'apple': 10, 'banana': 2, 'cherry': 7, 'date': 5}
ascending = dict(sorted(data.items(), key=lambda item: item[1]))
print("Ascending order by value:")
print(ascending)
descending = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("\nDescending order by value:")
print(descending)
