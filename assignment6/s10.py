# 10
print("\n10. Bonus calculation:")
salary = float(input("Enter salary: "))
years = int(input("Years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus:", bonus)
else:
    print("No bonus")