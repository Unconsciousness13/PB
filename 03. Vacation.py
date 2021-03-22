needed_money = float(input())
owned_money = float(input())
days_counter = 0
spend_counter = 0
while owned_money < needed_money and spend_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        owned_money += money
        spend_counter = 0
    elif command == "spend":
        owned_money -= money
        spend_counter += 1
        if owned_money < 0:
            owned_money = 0
    if spend_counter == 5:
        print("You can't save the money.")
        print(f"{days_counter}")
    if owned_money >= needed_money:
        (print (f"You saved the money for {days_counter} days."))
