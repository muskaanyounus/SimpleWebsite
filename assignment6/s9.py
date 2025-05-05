# 9
print("\n9. Calculate cost with discount:")
quantity = int(input("Enter quantity: "))
cost = quantity * 100
if cost > 1000:
    cost *= 0.9
print("Total cost:", cost)