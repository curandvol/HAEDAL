from datetime import datetime

now = datetime.now()
a = str(now.year)
b = str(now.month)
c = str(now.day)
year_a = a.zfill(4)
month_b = b.zfill(2)
day_c = c.zfill(2)
print("{0}-{1}-{2}".format(year_a, month_b, day_c))