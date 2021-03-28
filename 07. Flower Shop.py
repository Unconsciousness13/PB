import math
magnolias = int(input())
hyacinth = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())
magnolias_price = 3.25
hyacinth_price = 4
roses_price = 3.50
cactus_price = 8
price_flowers = (magnolias * magnolias_price) + (hyacinth * hyacinth_price) + (roses * roses_price) + (
            cactus * cactus_price)
price_flowers *= 0.95
total = abs(gift_price - price_flowers)
if gift_price <= price_flowers:
    print (f"She is left with {math.floor(total)} leva.")
else:
    print (f"She will have to borrow {math.ceil(total)} leva." )
