#!/usr/bin/env python3
# Student ID: 146631213
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return a normalized sum."""
    sum = Time()

    # Add raw values
    sum.second = t1.second + t2.second
    sum.minute = t1.minute + t2.minute
    sum.hour = t1.hour + t2.hour

    # Normalize seconds to minutes
    if sum.second >= 60:
        carry_min = sum.second // 60
        sum.second = sum.second % 60
        sum.minute += carry_min

    # Normalize minutes to hours
    if sum.minute >= 60:
        carry_hr = sum.minute // 60
        sum.minute = sum.minute % 60
        sum.hour += carry_hr

    return sum


def change_time(time, seconds):
    
    # Convert current time to total seconds
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second + seconds

    # Prevent negative time
    if total_seconds < 0:
        total_seconds = 0

    # Convert back to hours, minutes, seconds
    time.hour = total_seconds // 3600
    time.minute = (total_seconds % 3600) // 60
    time.second = total_seconds % 60

    return None

...
...
def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time
...
...


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
