'''
from datetime import date,time,date
today = date.today()
print(today)

print(date(2026,3,31))
print(date(20206,22,30))    # print error 
print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)

#weekday() → gives day from 0 to 6
#Monday = 0, Sunday = 6)
print(today.weekday())

#isoweekday() → gives day from 1 to 7
#Monday = 1, Sunday = 7)
print(today.isoweekday())

--------------------------------------------------
#  Create custom time
from datetime import datetime, time
now = time(21,56,18)  #time(h, m, s) → create time
print(now.hour)
print(now.minute)
print(now.second)
----------------------------------------------------

# Current date and time
from datetime import datetime
now = datetime.now()
print(now)
----------------------------------------------------

# Different formats
from datetime import datetime
now = datetime.now()
print(now.strftime('%d/%m/%y %H:%M:%S'))
print(now.strftime('%d/%m/%y %I:%M:%S'))
print(now.strftime('%d %b %y %I:%M:%S'))
print(now.strftime('%d %B %y %I:%M:%S'))
print(now.strftime('%d %B %y %I:%M:%S %p'))
print(now.strftime('%A, %d %B %y %I:%M:%S %p'))

%d → day
%y → year
%m → month number
%b → short month
%B → full month
%y → year
%H → 24 hr
%I → 12 hr
%p → AM/PM
%A → day name
-------------------------------------------------
'''

## timedelta - used to add or subtract time
from datetime import date,datetime,timedelta
today = date.today()
now = datetime.now()
today_7 = today-timedelta(days=7)
print(today_7)
# Subtracts 7 days from today, means: date before 7 days


now_30 = now+timedelta(minutes=30)
print(now_30)
# Adds 30 minutes to current time, means: time after 30 minutes


