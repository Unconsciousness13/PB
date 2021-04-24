budged = float(input())
fuel_need = float(input())
day_of_week = input()


fuel_liter = 2.10
guide_price = 100

fuel_total = fuel_liter * fuel_need
total = (fuel_total + guide_price)

if day_of_week == "Saturday":
    total *= 0.90
if day_of_week == "Sunday":
    total *= 0.80

diff = (budged - total)
if diff >= 0:
    print(f"Safari time! Money left: {abs(diff):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")
