screen_type = input()
rows = int(input())
columns = int(input())
size = columns * rows
income = 0
if screen_type == "Premiere":
    income = size * 12

elif screen_type == "Normal":
    income = size * 7.50
elif screen_type == "Discount":
    income = size * 5
print (f"{income:.2f}")
