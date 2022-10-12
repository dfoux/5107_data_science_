import csv
import pandas
from SETTINGS.display_settings import display

csv_file_path = "..\\Sales_Month_Data\\2021\\Sales_September_2021.csv"

table_break = "\n" + "#" * 122 + "\n"


def new_table():
    f = open(csv_file_path, "w", newline="")
    header = ("Order ID", "Product", "Quantity Ordered", "Price Each", "Order Date", "Purchase Address")
    empty_tuple = ("", "", "", "", "", "")
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(empty_tuple)
    f.close()


def read_single_csv():
    single_csv = pandas.read_csv(csv_file_path)
    # print(single_csv.head(20))
    # print(table_break)
    print(single_csv.tail(20))


display()
new_table()
print(table_break)
read_single_csv()
print(table_break)
