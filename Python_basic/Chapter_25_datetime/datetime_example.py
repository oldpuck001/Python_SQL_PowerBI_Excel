# datetime_py.py

import datetime as dt

# dt.datetime(year, month, day, hour, minute, second, microsecond, timezone)

timestamp = dt.datetime(2020, 1, 31, 14, 30)

print(timestamp)

print(timestamp.day)

print(timestamp - dt.datetime(2020, 1, 14, 12, 0))

print(timestamp + dt.timedelta(days=1, hours=4, minutes=11))

print(timestamp.strftime('%d/%m/%Y %H:%M'))

print(f'{timestamp:%d/%m/%Y %H:%M}')

print(dt.datetime.strptime('12.1.2020', '%d.%m.%Y'))