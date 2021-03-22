month = input()
night_stay = int(input())
apartment = 0
studio = 0
if month == "May" or month == "October":
    studio = 50 * night_stay
    apartment = 65 * night_stay
    if 7 < night_stay < 14:
        studio *= 0.95
    elif night_stay > 14:
        studio *= 0.70
elif month == "June" or month == "September":
    studio = 75.2 * night_stay
    apartment = 68.7 * night_stay
    if night_stay > 14:
        studio *= 0.80
elif month == "July" or month == "August":
    studio = 76 * night_stay
    apartment = 77 * night_stay
if night_stay > 14:
    apartment *= 0.90

print (f"Apartment: {apartment:.2f} lv.")
print (f"Studio: {studio:.2f} lv.")
