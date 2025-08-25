def add_time(start, duration, day = None):
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if am_pm == 'PM':
        start_hour += 12

    total_minutes = start_minute + duration_minute
    new_minute = total_minutes % 60
    minute_carry_over = total_minutes // 60

    total_hours = start_hour + duration_hour + minute_carry_over
    new_hour_24 = total_hours % 24
    days_later = total_hours // 24

    new_am_pm = 'AM'
    new_hour_12 = new_hour_24

    if new_hour_24 >= 12:
        new_am_pm = 'PM'

    if new_hour_24 > 12:
        new_hour_12 = new_hour_24 - 12
    elif new_hour_24 == 0:
        new_hour_12 = 12

    new_minute_str = f'{new_minute:02d}'

    new_time_str = f'{new_hour_12}:{new_minute_str} {new_am_pm}'
    
    week_days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    reverse_week_days = {v: k.capitalize() for k, v in week_days.items()}

    if day:
        start_day_num = week_days[day.lower()]
        new_day_num = (start_day_num + days_later) % 7
        new_day = reverse_week_days[new_day_num]
        new_time_str += f', {new_day}'

    if days_later == 1:
        new_time_str += ' (next day)'
    elif days_later > 1:
        new_time_str += f' ({days_later} days later)'
    print(new_time_str)
    return new_time_str

add_time('8:16 PM', '466:02', 'Tuesday')