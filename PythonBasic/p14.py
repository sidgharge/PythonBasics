from datetime import date

f_date = date(2018, 5, 2)
s_date = date(2018, 4, 30)

date_diff = f_date - s_date

print(date_diff.days)
