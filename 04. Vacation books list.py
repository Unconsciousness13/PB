total_pages = int(input())
pages_per_hour = int(input())
days = int(input())
needed_time = total_pages / pages_per_hour
daily_hours = needed_time / days
print(daily_hours)