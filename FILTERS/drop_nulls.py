import pandas
from SETTINGS.display_settings import display

table_break = "\n" + "#" * 122 + "\n"

merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"
all_data = pandas.read_csv(merged_csv_path)


def drop_null_rows():
    list_nulls = all_data[all_data.isna().any(axis=1)]
    remove_nulls = all_data.dropna(how='all')  # or how='any'
    print(table_break)
    print(list_nulls.head(50))
    print(table_break)
    print(remove_nulls.head(50))
    print(table_break)


display()
drop_null_rows()
