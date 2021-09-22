import datetime

x = datetime.datetime.now()

print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond, x.tzinfo)

xxx = f"{x.year}{x.month}{x.day}{x.hour}{x.minute}{x.second}{x.microsecond}"
print(xxx)

