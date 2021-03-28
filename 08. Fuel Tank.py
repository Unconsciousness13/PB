fuel_type = input()
fuel_quantity = int(input())
if fuel_type == "Diesel" and fuel_quantity >= 25:
    print(f"You have enough {(str.lower(fuel_type))}.")
elif fuel_type == "Diesel" and fuel_quantity < 25:
    print(f"Fill your tank with {(str.lower(fuel_type))}!")
elif fuel_type == "Gas" and fuel_quantity >= 25:
    print(f"You have enough {(str.lower(fuel_type))}.")
elif fuel_type == "Gas" and fuel_quantity < 25:
    print(f"Fill your tank with {(str.lower(fuel_type))}!")
elif fuel_type == "Gasoline" and fuel_quantity >= 25:
    print(f"You have enough {(str.lower(fuel_type))}.")
elif fuel_type == "Gasoline" and fuel_quantity < 25:
    print(f"Fill your tank with {(str.lower(fuel_type))}!")
else:
    print("Invalid fuel!")
