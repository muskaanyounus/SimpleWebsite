# 11
print("\n11. Grade system:")
marks = int(input("Enter marks: "))
if marks < 25:
    print("F")
elif marks <= 45:
    print("E")
elif marks <= 50:
    print("D")
elif marks <= 60:
    print("C")
elif marks <= 80:
    print("B")
else:
    print("A")