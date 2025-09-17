"""
Author: David Cheeseman
Date: 2025-09-17
"""
import re

# Keep track of time in minutes since that's the smallest unit Steam tracks
total_minutes = 0

# Read the file
with open('steam_hours.txt') as f:
    for line in f:
        # If you're reading your own profile, LAST PLAYED will be populated
        if 'LAST PLAYED' in line:
            match = re.search(r'TOTAL PLAYED(.*?)LAST PLAYED', line)
        else:
            # Otherwise, for friends, it won't
            match = re.search(r'TOTAL PLAYED(.*)', line)
        
        # Ensure we have a parsable match
        if not match:
            continue
        time_str = match.group(1).strip()
        if not time_str:
            continue

        # Separate time and units and sum time in minutes
        time, units = time_str.split()
        if units == 'hours':
            total_minutes += 60 * float(time.replace(",",""))
        elif units == 'minutes':
            total_minutes += float(time.replace(",",""))

# Subtract out duplicate hours here. Example:
# total -= 125.3 * 60 # Subtract 125.3 hours, from blender for example

# Make human readable
year = 24*60*365.25
day = 24*60
years = int(total_minutes / year)
total_minutes -= years * year
days = int(total_minutes / day)
total_minutes -= days * day
hours = int(total_minutes/60)
total_minutes -= hours * 60
minutes = int(total_minutes)

print(f"Total Steam Time: {years} year(s) {days} day(s) {hours} hour(s) {minutes} minute(s)")
