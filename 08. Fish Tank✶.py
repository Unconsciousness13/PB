lenght_cm = float(input())
width_cm = float(input())
height_cm = float(input())
volume_precentage = float(input())
volume_precentage = volume_precentage * 0.01
volume_total = (lenght_cm * width_cm * height_cm)
liters_total = volume_total * 0.001
water_liters = (liters_total * (1 - volume_precentage))
print(water_liters)
