hours = int(input())
minutes = int(input())
current_time_in_minutes = hours * 60 + minutes
time_after_fifteen_minutes = current_time_in_minutes + 15
hours_after_fifteen_minutes = time_after_fifteen_minutes // 60
minutes_after_fifteen_minutes = time_after_fifteen_minutes % 60
if hours_after_fifteen_minutes > 23:
    hours_after_fifteen_minutes -= 24
if minutes_after_fifteen_minutes < 10:
    print (f"{hours_after_fifteen_minutes}:0{minutes_after_fifteen_minutes}")
else:
    print (f"{hours_after_fifteen_minutes}:{minutes_after_fifteen_minutes}")
# current_minutes_sum = current_minutes + 15
# current_hours_after = current_minutes_sum // 60
# current_minutes_after = current_minutes_sum % 60
# if current_hours_after > 23: current_hours_after -= 24
# if current_minutes_sum > 10:
#     print (f"{current_hours_after}:0{current_minutes_sum}")
# else:
#     print (f"{current_hours_after}:{current_minutes_after}")
