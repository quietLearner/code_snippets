import datetime

# https://arrow.readthedocs.io/en/latest/

# pip install tzdata
from zoneinfo import ZoneInfo
import zoneinfo

# pip install pytz, not recommended by python anymore, use zoneinfo
# import pytz

x = datetime.date(2020, 5, 17)
print(x)

tday = datetime.date.today()
print(tday.year, tday.month, tday.day, tday.weekday(), tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday - tdelta, tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 +- date2

bday = datetime.date(2025, 12, 2)

till_bday = bday - tday
print(till_bday.days, till_bday.total_seconds(), till_bday)


t = datetime.time(9, 30, 45, 100000)
print(t, t.hour)


dt = datetime.datetime(2016, 7, 24, 12, 30, 45, 100000)
print(dt, dt.date(), dt.time())


today = datetime.datetime.today()
now = datetime.datetime.now(tz=datetime.timezone.utc)
utcnow = datetime.datetime.utcnow()
print(today)
print(now)
print(utcnow)


dt_utc = datetime.datetime(2016, 7, 27, 12, 30, 45, 2000, tzinfo=datetime.timezone.utc)
print(dt_utc)


dt_toronto = dt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=-5)))
print(dt_toronto)

dt_toronto_1 = dt_utc.astimezone(ZoneInfo("America/Toronto"))
print(dt_toronto_1)


for tz in zoneinfo.available_timezones():
    print(tz)

local_time = datetime.datetime.now()
print(local_time)


dt_los_angeles = local_time.astimezone(ZoneInfo("America/Los_Angeles"))
print(dt_los_angeles)

print(dt_los_angeles.isoformat())


print(dt_los_angeles.strftime("%B %d, %Y"))

dt_str = "July 26, 2016"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
