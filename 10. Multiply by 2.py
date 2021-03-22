number = 0
while number >= 0:
    number = float(input())
    number *= 2
    print(f"{number:.2f}")
else:
    print("Negative number!")