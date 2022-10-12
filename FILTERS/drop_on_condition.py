import pandas
from SETTINGS.display_settings import display

table_break = "\n" + "#" * 122 + "\n"

merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"


def drop_on_condition():  # will also drop nulls
    all_data = pandas.read_csv(merged_csv_path)
    where = 'Product'
    condition = 'hmm'
    all_data = all_data.dropna(how='all')  # or how='any'
    all_data.drop(all_data[all_data[where] == condition].index, inplace=True)

    print(table_break)
    print(all_data.head(200))
    print(table_break)


display()
drop_on_condition()
