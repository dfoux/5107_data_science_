import pandas

directory_path = "../Sales_Month_Data/2019"
merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"

all_data = pandas.read_csv(merged_csv_path)


def group_products():

    final_data = all_data.drop(['Order ID'], axis = 1)
    final_data_ren = final_data.rename(columns={'Price Each': 'Sales'}, index={'ONE': 'Row_1'})
    final_data_ok = final_data_ren.groupby('Product').sum()
    return final_data_ok


print(group_products())
