flowers_type = input()
flowers_unit = int(input())
budget = int(input())
total_sum = 0
price = 0
if flowers_type == "Roses":
    price = 5
    if flowers_unit > 80:
        price *= 0.90
elif flowers_type == "Dahlias":
    price = 3.80
    if flowers_unit > 90:
        price *= 0.85
elif flowers_type == "Tulips":
    price = 2.80
    if flowers_unit > 80:
        price *= 0.85
elif flowers_type == "Narcissus":
    price = 3
    if flowers_unit < 120:
        price *= 1.15
elif flowers_type == "Gladiolus":
    price = 2.50
    if flowers_unit < 80:
        price *= 1.20
total_sum = flowers_unit * price
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {flowers_unit} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
