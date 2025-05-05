# 12
print("\n12. Attendance check:")
classes_held = int(input("Classes held: "))
classes_attended = int(input("Classes attended: "))
percentage = (classes_attended / classes_held) * 100
print("Attendance:", percentage, "%")
if percentage < 75:
    print("Not allowed to sit in exam")
else:
    print("Allowed to sit in exam")