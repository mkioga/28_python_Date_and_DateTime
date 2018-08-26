
# =========================
# 28_Date_and_DateTime.py
# =========================

# "time" module

# First we will look at options in "time" module
# Even if "time" module includes dates, if you are dealing with dates a lot
# it is better to use "datetime" module

# TimeZones

# We will look at the "timezone" support that exist in the current "time" module
# We can get information about the current timezone via "time.timezone" and "time.tzname"
# These are not functions but offset values

# "time.tzname"

# "time.tzname" returns the name of your timezone e.g. Central Standard or Central Daylight etc.
# it returns a tuple countaining two strings. first is Non-DST timezone (e.g. Central Standard time)
# and name of DST-Timezone (e.g. Central Daylight Time)

# =================
# "time.timezone"
# =================

# "time.timezone" returns the the number of seconds offset from UTC
# This will be Negative for countries east of GMT and positive for countries west of GMT
# It uses the "Non-Daylight Saving time (Non-DST)" when calculating the offset.
# So you must check to see if Daylight Savings is in effect and then apply the correction.


# before relying on "time.timezone", you need to check the value of "time.daylight"
# if this is Non-Zero, then DST-Timezone is defined and
# you can trust at that point the second string in the "time.tzname" tuple, otherwise you should not use the second string.

# Example


import time

# time.strftime = string formatted time
# time.gmttime(0) is GMT time from the first possible date. i.t. epoch (1970)
# '%c' is a replacement field to convert to lower case

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print()

# time.tzname[0] is the Non-DST time
# time.tzname[1] is the DST time
print("time.tzname[0] returns Non-DST time which is : {}".format(time.tzname[0]))
print("time.tzname[1] returns DST time which is     : {}".format(time.tzname[1]))
print()

# time.daylight is Nonzero if a DST timezone is defined

print("time.daylight returns: '{}'".format(time.daylight))
print()

print("My current timezone is '{0}' with an offset of {1}".format(time.tzname[0], time.timezone))
print()

if time.daylight != 0:
    print("Daylight Saving time is in effect for this location")
    print("The DST timezone is: " + time.tzname[1])

print()

# Now we print local time and GMT time and extract year, month, day, hour, minute, seconds
# The parameters for strftime() are in this link
# https://docs.python.org/2/library/time.html#time.strftime
# '%Y-%m-%d %H:%M:%S' represents Year, Month, Hour, Minute, Seconds

print("Local time is: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is:   " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
print()

print("="*40)

# ===================
# "datetime" module
# ===================

# We will use the "datetime" module if we are dealing with Dates and Time
# Here is documentation for "datetime" module
# https://docs.python.org/2/library/datetime.html

# https://docs.python.org/2/library/datetime.html
# "naive" is not aware of daylight savings while "aware" is aware of daylight savings.

# Note that there is a "datetime" module and a "datetime" class which is extracted with datetime.datetime


import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print("="*40)

# datetime.tzinfo" get more info on this link
# https://docs.python.org/2/library/datetime.html#datetime.tzinfo

# =========
# pip
# =========

# if you go to command prompt and type "pip" and get a message that it is not recognized
# you need to modify python installation and check "pip" and "Add python to environment variables.
# instructions are on these links
# for PC
# https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/4436368?start=0
# For MAC
# https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/4436372?start=0

# =======
# "pytz"
# =======

# This link will show you how to install "pytz" (Python Timezone Package or library)
# https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/4466600?start=0
# https://pypi.python.org/pypi/pytz

# Now we are going to use the "pytz" module because we have installed it.

import pytz
import datetime

# We define the city by using format "Continent/City". Note they start with Caps

berlin = "Europe/Berlin"
madrid = "Europe/Madrid"
nairobi = "Africa/Nairobi"
lagos = "Africa/Lagos"
minneapolis = "US/Central"  # for US, we use Central, Eastern, Mountain etc and not city

# ptyz.timezone(city) returns result in format "Continent/City"

europe_berlin = pytz.timezone(berlin)
europe_madrid = pytz.timezone(madrid)
africa_nairobi = pytz.timezone(nairobi)
africa_lagos = pytz.timezone(lagos)
us_minneapolis = pytz.timezone(minneapolis)

# We print them here to see

print(europe_berlin)
print(europe_madrid)
print(africa_nairobi)
print(africa_lagos)
print(us_minneapolis)

print("="*40)

# Now we use module "datetime.datetime.now() to get local time in those cities

berlin_time = datetime.datetime.now(europe_berlin)
madrid_time = datetime.datetime.now(europe_madrid)
nairobi_time = datetime.datetime.now(africa_nairobi)
lagos_time = datetime.datetime.now(africa_lagos)
minneapolis_time = datetime.datetime.now(us_minneapolis)

print()
print("Time in '{}' is : {}".format(berlin, berlin_time))
print("Time in '{}' is : {}".format(madrid, madrid_time))
print("Time in '{}' is: {}".format(nairobi, nairobi_time))
print("Time in '{}' is  : {}".format(lagos, lagos_time))
print("Time in '{}' is    : {}".format(minneapolis, minneapolis_time))
print("UTC time is                : {}".format(datetime.datetime.utcnow()))

print("="*40)

# Another way to extract timezones is to use "tz=city"

berlin_time_tz = datetime.datetime.now(tz=europe_berlin)
madrid_time_tz = datetime.datetime.now(tz=europe_madrid)
nairobi_time_tz = datetime.datetime.now(tz=africa_nairobi)
lagos_time_tz = datetime.datetime.now(tz=africa_lagos)
minneapolis_time_tz = datetime.datetime.now(tz=us_minneapolis)


print()
print("Time in '{}' is : {}".format(berlin, berlin_time_tz))
print("Time in '{}' is : {}".format(madrid, madrid_time_tz))
print("Time in '{}' is: {}".format(nairobi, nairobi_time_tz))
print("Time in '{}' is  : {}".format(lagos, lagos_time_tz))
print("Time in '{}' is    : {}".format(minneapolis, minneapolis_time_tz))
print("UTC time is                : {}".format(datetime.datetime.utcnow()))

print()
print("="*40)

# pytz.all_timezones

# you can print the entire list of what pytz accepts using pytz.all_timezones

print("== print pytz.all ==")
print()
for i in pytz.all_timezones:
    print(i)

print("="*60)
print()
# We can also print all countries and their IO3166 country codes
print("== print all countries and their 103166 country codes ==")
print()

for x in sorted(pytz.country_names):
    print(x + ":" + pytz.country_names[x])

print("="*40)

# Some countries have different timezones.
# you can extract different timezones for countries using ptyz.country_timezones
print("== ptyz.country_timezones ===")
print()

print("Code: Country: Country_Time_Zones:")
print()

# NOTE: This will give an error when you reach BV because there is no time defined
# for Bouvet Island in Netherlands
#

# NOTE: Commented below code out because it gives error for Bouvet Island


# import pytz
# import datetime
#
# for x in sorted(pytz.country_names):
#          print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
#
# # we can avoid the error by testing for countries that have no timezone if we know them
#
# for x in sorted(pytz.country_names):
#     if x != "BV" and x != "HM": # Here we are excluding BV and HM and it prints well
#         print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
#
#
print("="*40)







#
# ptyz gets timezone info from IANA (see link below)
# https://www.iana.org/time-zones
#
# A better method is using "get" method which returns "none" instead of error
# when the key does not have a value
# Note that get(x) uses (x) instead of [x]
# Note that BV returns None and not an error

import pytz
import datetime

print("=== Code: Country: Country_Time_Zones ===")
print()
for x in sorted(pytz.country_names):
        print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

print("="*40)




# Instead of using default "None" from get() like above code, you can test for
# existance of timezone and then write a message saying "No timezone defined" if we find none

import pytz
import datetime

print("==== Code: Country: Country_Time_Zones ====")
print("=" *40)

for x in sorted(pytz.country_names):
        print("{}: {}".format(x, pytz.country_names[x]), end=': ') # end= : because you want print below in same line as this
        if x in pytz.country_timezones:
            print(pytz.country_timezones[x])
        else:
            print("No Timezone defined") # We see this prints for BV which has no timezone



print("="*40)


# We can also print local time for each country


import pytz
import datetime

print("==== Code: Country: Country_Time_Zones: Local Time ====")
print()

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ') # end= : because you want print below in same line as this
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            timezone_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=timezone_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo Timezone defined") # We see this prints for BV which has no timezone

print("="*40)


# We have seen how to convert UTC time to local time using pytz
# It is very difficult to convert local time to UTC unless you know the timezone of the local time
# Best practice is to immediately convert time to UTS, work with UTC in your program and then
# convert it back to localtime to display to your users.

# In our examples above, all times printed were "naive" i.e. there was no timezones associated with the time

# pytz has a localized function that can be used to convert "naive" local datetime into "aware" datetime

import datetime
import pytz

# Naive time

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print()
print("Naive local time : {}".format(local_time))
print("Naive UTC time   : {}".format(utc_time))

print("="*40)

# # Now we are going to create "Aware" time using pytz.utc.localize().astimezone() function

aware_local_time = pytz.utc.localize(local_time).astimezone()  # Gives local time
aware_utc_time = pytz.utc.localize(utc_time)

# Note that tzinfo() is for timezone info
# Note that "aware" time has - 06:00 for US central time. This tells that local central time is 6 hours behind UTC
print()
print("Aware local time: {} = Timezone: {}".format(aware_local_time, aware_local_time.tzinfo)) # Gives local time
print("Aware UTC time  : {} = Timezone: {}".format(aware_utc_time, aware_utc_time.tzinfo)) # Gives UTC time
print()
print("="*40)


# fromtimestamp() vs utcfromtimestamp()
# fromtimestamp() pulls local time where you are while utcfromtimestamp() pulls UTC


gap_time = datetime.datetime(2018, 3, 4, 8, 55, 0, 0)
print("gap_time is:        {}".format(gap_time))     # prints time defined above
print("gap_time timestamp: {}".format(gap_time.timestamp()))  # Seconds from 1970 to gap_time


s = 1445733000   # defining seconds from epoch
t = s + (60 * 60)  # Then we add 5 hour to it.

print()
gb = pytz.timezone("GB")  # gb is time zone for Great Britain

# These two lines are supposed to give same answer because they are using fromtimestamp()
# fromtimestamp() gives local time corresponding to timestamp
# However mine shows the time difference of one hour as expected.
# May work in some timezones but may not work in others

dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print("{} seconds since epoch is {}".format(s, dt1))
print("{} seconds since epoch is {}".format(s, dt2))

print("="*40)


# # A better way is to use utcfromtimestamp() to work in UTC time and it will be accurate in all timezones

dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print()
print("{} seconds since epoch is {}".format(s, dt1))  # shows offset 01:00
print("{} seconds since epoch is {}".format(s, dt2))  # Shows offset 00:00

print("="*40)

# If you are writing code to deal with many timezones, you can use virtual machines
# which you can set to different to test your code.



# DateandTime Challenge

# Create a program that allows a user to use one of up to 9 timezones from a menu
# You can choose any zones you want from the all_timezones list

# The program will then display the time in that timezone as well as the local time and UTC time
# Entering 0 as a choice will quit the program

# Display the dates and times in a format suitable for the users of your program to understand
# and include the timezone name when displaying the chosen time.

import datetime
import pytz

# We create a dictionary to store the available timezones

available_timezones = {'1': "Africa/Nairobi",
                       '2': "Asia/Kolkata",
                       '3': "Australia/Adelaide",
                       '4': "Europe/Paris",
                       '5': "Japan",
                       '6': "Pacific/Tahiti",
                       '7': "US/Central",
                       '8': "Europe/London",
                       '9': "Zulu"}


# Now we use a for loop to print out the available timezones using the key

print("These are the available timezones:")
for place in sorted(available_timezones):
    print("\t{}: {}".format(place, available_timezones[place]))

print("="*20)

# Now we ask the user to choose a timezone.
# If they choose 0, the program quits

print()
print("Please enter a timezone (0 to quit): ")

# We take above input and assign it to variable "choice"
# Then test if choice == 0 and break
# Remember string format time presentation (strftime)
# https://docs.python.org/2/library/time.html#time.strftime
# %A = Full weekday name, %x = date, %X = time, %z = hour/minute offset from GMT

while True:    # if there is an input entered by user
    choice = input()   # Take user input and assign it to choice

    if choice == '0':    # if choice is 0, break
        break

    if choice in available_timezones.keys():   # if choice is in available_timezones keys
        timezone_to_display = pytz.timezone(available_timezones[choice])  # find available timezones chosen
        world_time = datetime.datetime.now(tz=timezone_to_display)

        print("The time in '{}' is '{}' : '{}'".format(available_timezones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))

print("="*40)
