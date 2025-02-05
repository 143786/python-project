def min_sec_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours


print(min_sec_to_hours(120, 20))

