budged = float(input())
season = input()
price = 0
if budged <= 100:
    if season == "summer": # Bulgaria
        price = budged * 0.70
        print ("Somewhere in Bulgaria")
        print (f"Camp - {budged-price:.2f}")
    elif season == "winter":
        price = budged * 0.30
        print("Somewhere in Bulgaria")
        print(f"Hotel - {budged - price:.2f}")
elif 100 < budged <= 1000: #Bolkans
    if season == "summer":
        price = budged * 0.60
        print("Somewhere in Balkans")
        print(f"Camp - {budged - price:.2f}")
    elif season == "winter": #Europe
        price = budged * 0.20
        print("Somewhere in Balkans")
        print(f"Hotel - {budged - price:.2f}")
elif budged > 1000:
    price = budged * 0.10
    print("Somewhere in Europe")
    print(f"Hotel - {budged - price:.2f}")


