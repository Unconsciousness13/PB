budged = float(input())
command = input()

product_count = 0
total = 0

while command != "Stop":
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price *= 0.50

    total += product_price

    if total > budged:
        print("You don't have enough money!")
        print(f"You need {abs(total - budged):.2f} leva!")
        break
    command = input()
    if command == "Stop":
        print(f"You bought {product_count} products for {total:.2f} leva.")
        break