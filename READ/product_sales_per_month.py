import pandas
from SETTINGS.display_settings import display

compl_table_break = "\n" + "#" * 146 + "\n"
short_table_break = "\n" + "#" * 15 + "\n"

directory_path = "../Sales_Month_Data/2019"
merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"


def read():
    global all_data
    all_data = pandas.read_csv(merged_csv_path)


def convert_fields_to_num():
    field_1 = 'Quantity Ordered'
    field_2 = 'Price Each'
    all_data[field_1] = pandas.to_numeric(all_data[field_1])  # Make int
    all_data[field_2] = pandas.to_numeric(all_data[field_2])  # Make float


def group_month():
    all_data['Month'] = all_data['Order Date'].str[3:5]
    all_data['Month'] = all_data['Month'].astype('int32')
    return all_data.head(100)


def month_sales_list():
    all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
    return all_data.groupby('Month').sum()[['Sales']]


display()
read()
convert_fields_to_num()
print(compl_table_break)
print(group_month())
print(compl_table_break)
print(month_sales_list())
print()
print(short_table_break)
