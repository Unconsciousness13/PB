fuel_type = input()
fuel_quantity = float(input())
club_card = input()
gas = 0.93
gasoline = 2.22
diesel = 2.33
price = 0
if fuel_type == "Gas"  and club_card == "Yes":
    gas = 0.85
    price = gas * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
elif fuel_type == "Diesel"  and club_card == "Yes":
    diesel = 2.21
    price = diesel * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
elif fuel_type == "Gasoline"  and club_card == "Yes":
    gasoline = 2.04
    price = gasoline * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
elif fuel_type == "Gas"  and club_card == "No":
    price = gas * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
elif fuel_type == "Diesel"  and club_card == "No":
    price = diesel * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
elif fuel_type == "Gasoline"  and club_card == "No":
    price = gasoline * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        price *= 0.92
    elif fuel_quantity > 25:
        price *= 0.90
    print (f"{price:.2f} lv.")
