junior_group = int(input())
senior_group = int(input())
type_race = input()
juniors_price = 0
seniors_price = 0
total_units = junior_group + senior_group
total_sum = 0
if type_race == "trail":
    juniors_price = 5.50
    seniors_price = 7
elif type_race == "cross-country":
    juniors_price = 8
    seniors_price = 9.50
elif type_race == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif type_race == "road":
    juniors_price = 20
    seniors_price = 21.50
total_sum = (junior_group * juniors_price) + (senior_group * seniors_price)
if type_race == "cross-country" and total_units >= 50:
    total_sum *= 0.75
total_sum *= 0.95
print (f"{total_sum:.2f}")

