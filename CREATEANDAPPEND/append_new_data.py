import csv
import pandas
from SETTINGS.display_settings import display

display()

csv_file_path = "../Sales_Month_Data/2021/Sales_September_2021.csv"

table_break = "\n" + "#" * 122 + "\n"


def add_row():

    f = open(csv_file_path, "a", newline="")

    # new_tuple = (Order ID, "Product", Quantity Ordered, Price Each, "Order Date", "Purchase Address")
    new_tuple = (24, "apples", 1, 149.99, "06/06/19 10:21", "Lisboa, Portugal")
    # new_tuple = ("","","","","","")
    # new_tuple = ("hmm", "hmm", "hmm", "hmm", "hmm", "hmm")

    writer = csv.writer(f)
    writer.writerow(new_tuple)
    f.close()


def read_single_csv():
    single_csv = pandas.read_csv(csv_file_path)
    print(single_csv.head(5))
    print(table_break)
    print(single_csv.tail(5))


add_row()
print(table_break)
read_single_csv()
print(table_break)
