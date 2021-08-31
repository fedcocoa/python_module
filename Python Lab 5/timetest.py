from math import pi

def time(total_sec):
    """>>> time(6149)
1 42 29
    """
    seconds = total_sec % 60
    total_minutes = total_sec // 60
    minutes = total_minutes % 60
    hours = total_minutes // 60
    print(hours,minutes,seconds)

def volume(rad):
    return (4*pi*rad**3)/3

def books(no,price,discount):
    if no > 0:
        return 3 + price*no*discount + .75*no-1
    else:
        return 0
