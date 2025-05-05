# 17
print("\n17. Even, odd and prime lists:")
even = []
odd = []
prime = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    if i > 1:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
print("Even:", even)
print("Odd:", odd)
print("Prime:", prime)
