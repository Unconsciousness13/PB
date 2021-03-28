import math
total_days = int(input())
food_count_in_kg = int(input())
dog_food_daily_kg = float(input())
cat_food_daily_kg = float(input())
turtle_food_daily_gr = float(input())
turtle_food_daily_kg = turtle_food_daily_gr / 1000
total_food = (total_days * dog_food_daily_kg) + (total_days * cat_food_daily_kg) + (total_days * turtle_food_daily_kg)
difference = food_count_in_kg - total_food
if food_count_in_kg >= total_food:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print (f"{math.ceil(abs(difference))} more kilos of food are needed.")
