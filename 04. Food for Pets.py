import math
days = int(input())
total_food = int(input())
daily_dog = 0
daily_cat = 0
daily_total = daily_cat + daily_dog
biscuit = 0
biscuit_tot = 0
for day in range(1, days + 1):
    dog = int(input())
    daily_dog += dog
    cat = int(input())
    daily_cat += cat
    if day % 3 == 0:
        biscuit = (dog + cat) * 10 / 100
        biscuit_tot += biscuit

rest_of_food = total_food - (daily_dog + daily_cat)
food_eaten = total_food - rest_of_food
print(f"Total eaten biscuits: {int(math.floor(biscuit_tot))}gr.")
print(f"{food_eaten/total_food *  100:.2f}% of the food has been eaten.")
print(f"{daily_dog / food_eaten * 100:.2f}% eaten from the dog.")
print(f"{daily_cat/food_eaten *  100:.2f}% eaten from the cat.")
