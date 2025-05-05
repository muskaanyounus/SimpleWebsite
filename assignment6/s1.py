# 1
print("1. Numbers divisible by 7 and multiple of 5 between 1500 and 2700:")
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")
print("\n")