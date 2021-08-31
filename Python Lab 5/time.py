def time(total_sec):
    """>>>time(6149)
    1 42 29
    """
    seconds = total_sec % 60
    total_minutes = total_sec // 60
    minutes = total_minutes % 60
    hours = total_minutes // 60
    print(hours,minutes,seconds)