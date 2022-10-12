import pandas
import matplotlib.pyplot as plt

directory_path = "../Sales_Month_Data/2019"
merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"

all_data = pandas.read_csv(merged_csv_path)
results = None


def split_month():
    global results
    all_data['Month'] = all_data['Order Date'].str[3:5]
    all_data['Month'] = all_data['Month'].astype('int32')
    all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
    results = all_data.groupby('Month').sum()


def bargraph_month():
    months = range(1, 13)
    plt.bar(months, results['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD($)')
    plt.xlabel('Month')
    plt.show()


split_month()
bargraph_month()
