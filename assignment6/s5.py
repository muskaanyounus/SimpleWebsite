# 5
print("\n5. Sum and average of numbers (enter 0 to stop):")
total = 0
count = 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    print("Sum:", total, "Average:", total / count)
else:
    print("No numbers entered.")