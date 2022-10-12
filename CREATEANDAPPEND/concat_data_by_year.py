import pandas
import os
from SETTINGS.display_settings import display

files_to_merge_dir = "../Sales_Month_Data/2019/"
output_file = "../Sales_Year_Data/Sales_Year_2019.csv"

table_break = "\n" + "#" * 122 + "\n"


def concatenate_data():
    files = [file for file in os.listdir(files_to_merge_dir)]

    all_months_data = pandas.DataFrame()

    for file in files:
        all_data = pandas.read_csv(files_to_merge_dir + file)
        all_months_data = pandas.concat([all_months_data, all_data])

    all_months_data.to_csv(output_file, index=False)


def read_all_data_merged_csv():
    all_data = pandas.read_csv(output_file)

    print(all_data.head(100))
    print(table_break)
    print(all_data.tail(100))


concatenate_data()
display()
print(table_break)
read_all_data_merged_csv()
print(table_break)
