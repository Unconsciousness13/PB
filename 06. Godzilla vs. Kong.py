budget = float(input())
statist = int(input())
price_statist_dress = float(input())
decor = budget * 0.10
if statist > 150:
    price_statist_dress = price_statist_dress * 0.90

difference = (budget - (statist * price_statist_dress) - decor)

if difference < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(difference):.2f} leva more.")
elif  difference >= 0:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
