Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
squares = {}
for x in range(1, n + 1):
squares[x] = x * x  # Store x as the key and x*x as the value
print(squares)
