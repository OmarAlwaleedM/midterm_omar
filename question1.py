# Question 1 — Fill in what the code prints

import datetime
a = 7
b = 2
today = datetime.datetime.today()       # 2026-02-27 (Friday)
day_of_week = today.weekday()           # Friday = 4 (Mon=0, Tue=1, Wed=2, Thu=3, Fri=4)
month_of_year = today.month             # February = 2
a = a + day_of_week                     # 7 + 4 = 11
b += month_of_year                      # 2 + 2 = 4

print(a)                                # 11
print(b)                                # 4
c = a + b                               # 11 + 4 = 15
print(c)                                # 15
d = "xyz" * (c//3)                      # "xyz" * (15//3) = "xyz" * 5
print(d)                                # xyzxyzxyzxyzxyz

# Answer:
# 11
# 4
# 15
# xyzxyzxyzxyzxyz