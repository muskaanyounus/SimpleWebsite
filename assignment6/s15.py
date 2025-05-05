# 15
print("\n15. Average and product until 'q':")
total = 0
count = 0
product = 1
while True:
    val = input("Enter number (or q to quit): ")
    if val.lower() == 'q':
        break
    num = int(val)
    total += num
    product *= num
    count += 1
if count > 0:
    print("Average:", total / count, "Product:", product)