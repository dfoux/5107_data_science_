import pandas
import matplotlib.pyplot as matplt

directory_path = "../Sales_Month_Data/2019"
merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"

all_data = pandas.read_csv(merged_csv_path)
results = None


def split_cities():
    global results

    def get_city(address):
        return address.split(',')[1]

    def get_region(address):
        return address.split(',')[2].split(' ')[1]

    all_data['Cities'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_region(x)})")
    final_data = all_data.drop(['Order ID', 'Quantity Ordered'], axis=1)
    final_data_ren = final_data.rename(columns={'Price Each': 'Sales'}, index={'ONE': 'Row_1'})
    results = final_data_ren.groupby('Cities').sum()
    return results


def bargraph_city():
    cities = [i for i, dataframe in results.groupby('Cities')]
    matplt.bar(cities, results['Sales'])
    matplt.xticks(cities, size=6)
    matplt.ylabel('Sales in USD($)')
    matplt.xlabel('City Name')
    matplt.show()


split_cities()
bargraph_city()
