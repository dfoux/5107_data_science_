import pandas
from SETTINGS.display_settings import display

table_break = "\n" + "#" * 122 + "\n"

# single_csv_path = "../Sales_Month_Data/2021/Sales_September_2021.csv"
single_csv_path = "../Sales_Month_Data/Sales_Year_2019.csv"


def read_single_csv():
    single_csv = pandas.read_csv(single_csv_path)

    print(single_csv.head(200))
    print(table_break)
    print(single_csv.tail(200))
    print(single_csv.shape)


display()
print(table_break)
read_single_csv()
print(table_break)
