fruit = input()
size_set = input()
number_sets = int(input())
if fruit == "Watermelon" or fruit == "Mango" or fruit == "Pineapple" or fruit == "Raspberry " and size_set == "big" \
        or size_set == "small":
   #dinq
    if fruit == "Watermelon" and size_set == "big":
        fruit = 28.70 * 5 * number_sets
    elif fruit == "Watermelon" and size_set == "small":
        fruit = 56 * 2 * number_sets
    #ananas
    if fruit == "Pineapple" and size_set == "big":
        fruit = 24.80 * 5 * number_sets
    elif fruit == "Pineapple" and size_set == "small":
        fruit = 42.10 * 2 * number_sets
    #mango
    if fruit == "Mango" and size_set == "big":
        fruit = 19.60 * 5 * number_sets
    elif fruit == "Mango" and size_set == "small":
        fruit = 36.66 * 2 * number_sets
    #malina
    if fruit == "Raspberry" and size_set == "big":
        fruit = 15.20 * 5 * number_sets
    elif fruit == "Raspberry" and size_set == "small":
        fruit = 20 * 2 * number_sets
#discount
if fruit >= 400 and fruit <= 1000:
    fruit = fruit * 0.85
elif fruit>1000:
    fruit = fruit * 0.50

print (f"{fruit:.2f} lv.")


