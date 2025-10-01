baby_seconds = 10**9

def seconds_to_years(seconds):
    baby_hours = baby_seconds/3600
    baby_days =baby_hours/24
    baby_years = baby_days/365

    return(baby_years)
print(seconds_to_years(baby_seconds))


