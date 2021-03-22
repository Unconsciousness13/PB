gradus = int(input())
day_time = input()
total = 0
if 10 <= gradus <= 18:
    if day_time == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif day_time == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif 18 < gradus <= 24:
    if day_time == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day_time == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif gradus >= 25:
    if day_time == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day_time == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print (f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
