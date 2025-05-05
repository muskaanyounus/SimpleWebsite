# 19
print("\n19. Separate ints, floats and strings from a list:")
mixed = [10, "hello", 3.14, 25, "world", 2.5, 42, True]
ints = []
floats = []
strings = []
for item in mixed:
    if isinstance(item, int) and not isinstance(item, bool):
        ints.append(item)
    elif isinstance(item, float):
        floats.append(item)
    elif isinstance(item, str):
        strings.append(item)
print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strings)