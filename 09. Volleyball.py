import math

type_of_year = input()
number_of_holidays = float(input())
weekend_in_his_town = float(input())
if type_of_year == "leap" or type_of_year == "normal":
    weeks = 48
    weeks_in_sofia = weeks - weekend_in_his_town
    saturday_games_in_sofia = weeks_in_sofia * 3 / 4
    weeks_in_sofia_on_holidays = number_of_holidays * 2 / 3
    total_games_in_sofia = saturday_games_in_sofia + weekend_in_his_town + weeks_in_sofia_on_holidays
    leap_year = (total_games_in_sofia * 1.15)
    if type_of_year == "leap":
        print(math.floor(leap_year))
    else:
        print(math.floor(total_games_in_sofia))
