import math

income = float(input())
grade = float(input())
min_wage = float(input())
excellent_scholarship = grade * 25
social_scholarship = min_wage * 0.35
if grade >= 5.50:
    if income < min_wage:
        if excellent_scholarship >= social_scholarship:
            print (f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
        else :
            print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
    else:
        print(f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
elif grade > 4.50:
    if income < min_wage:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
    else: print("You cannot get a scholarship!")
else: print("You cannot get a scholarship!")

