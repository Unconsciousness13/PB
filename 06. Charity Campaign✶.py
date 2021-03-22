days_number = float(input())
confectioner = float(input())
cakes_number = float(input())
waffles_number = float(input())
pancakes_number = float(input())
cakes = (cakes_number * 45)
waffles = (waffles_number * 5.80)
pancakes = (pancakes_number * 3.20)
day_cost = (cakes + waffles + pancakes)
day_cost_total = day_cost * confectioner
total_sum = day_cost_total * days_number
print(total_sum - total_sum * 0.125)