import math
record_in_seconds = float(input())
meter_distance = float(input())
time_in_sec_for_one_min = float(input())
total_distance = meter_distance * time_in_sec_for_one_min
meter_distance_slowing = meter_distance / 15
slowing =  math.floor(meter_distance_slowing) * 12.5
total_time = total_distance + slowing
time_to_reach =  total_time - record_in_seconds
if total_time >= record_in_seconds:
    print (f"No, he failed! He was {abs(time_to_reach):.2f} seconds slower.")
elif total_time < record_in_seconds:
    print (f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")