deposit = float(input())
months = int(input())
interest = float(input())
month_interest = deposit * interest *0.12
total_money = deposit + months * month_interest
print(total_money)