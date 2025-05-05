sample_dict = {
    'a': 10,
    'b': 50,
    'c': 30,
    'd': 70,
    'e': 20,
    'f': 90
}
top_3 = sorted(sample_dict.items(), key=lambda item: item[1], reverse=True)[:3]
print("Top 3 highest values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")
