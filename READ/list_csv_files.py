import os
import datetime
import re
directory_path = "../Sales_Month_Data/2019/"

table_break = "\n" + "#" * 30 + "\n"

months = {v: i for i, v in enumerate(["January", "February", "March", "April",
                                      "May", "June", "July", "August", "September",
                                      "October", "November", "December"], start=1)}

files = [file for file in os.listdir(directory_path)]


def month_order(v):
    _, month, year = v[:-4].split("_")
    year = int(year)
    month = months[month]
    return datetime.datetime(year=year, month=month, day=1)


files.sort(key=month_order)

print(table_break)
for file in files:

    print(file)
print(table_break)