budget = float(input())
ticket_type = input()
peoples_in_group_count = int(input())
ticket_price = 0
difference = 0
if ticket_type == "VIP":
    ticket_price = 499.99
elif ticket_type == "Normal":
    ticket_price = 249.99
if 1 <= peoples_in_group_count <= 4:
    budget *= 0.25
elif 5 <= peoples_in_group_count <= 9:
    budget *= 0.40
elif 10 <= peoples_in_group_count <= 24:
    budget *= 0.50
elif 25 <= peoples_in_group_count <= 49:
    budget *= 0.60
elif peoples_in_group_count > 50:
    budget *= 0.75
price = ticket_price * peoples_in_group_count
total = budget - price
if budget >= price:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(total):.2f} leva.")
