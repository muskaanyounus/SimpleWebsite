# 13
print("\n13. Average of 10 numbers:")
total = 0
for i in range(10):
    total += int(input(f"Enter number {i+1}: "))
print("Average:", total / 10)