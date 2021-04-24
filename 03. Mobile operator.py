contract_time = input()
type_of_contract = input()
mobile_internet = input()
months_for_pay = int(input())
price = 0
tax = 0
if contract_time == "one" and type_of_contract == "Small":
    tax = 9.98
elif contract_time == "one" and type_of_contract == "Middle":
    tax = 18.99
elif contract_time == "one" and type_of_contract == "Large":
    tax = 25.98
elif contract_time == "one" and type_of_contract == "ExtraLarge":
    tax = 35.99
if contract_time == "two" and type_of_contract == "Small":
    tax = 8.58
elif contract_time == "two" and type_of_contract == "Middle":
    tax = 17.09
elif contract_time == "two" and type_of_contract == "Large":
    tax = 23.59
elif contract_time == "two" and type_of_contract == "ExtraLarge":
    tax = 31.79
if mobile_internet == "yes":
    if tax <= 10:
        price = tax + 5.50
    elif tax <= 30:
        price += tax + 4.35
    elif tax > 30:
        price += tax + 3.85
else:
    price = tax
if contract_time == "two":
    price *= 0.9625
total = price * months_for_pay
print(f"{total:.2f} lv.")
