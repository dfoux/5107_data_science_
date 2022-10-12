import pandas
import matplotlib.pyplot as matplt

directory_path = "../Sales_Month_Data/2019"
merged_csv_path = "../Sales_Year_Data/Sales_Year_2019.csv"

all_data = pandas.read_csv(merged_csv_path)

quantity_ordered = None
products = None
prices = None


def split_product():
    global quantity_ordered, products, prices
    product_group = all_data.groupby('Product')
    quantity_ordered = product_group.sum()['Quantity Ordered']
    products = [i for i, frameofdata in product_group]
    prices = all_data.groupby('Product').mean()['Price Each']


def set_bar_plot_properties():
    fig, ax1 = matplt.subplots()
    ax2 = ax1.twinx()
    ax1.bar(products, quantity_ordered, color='green')
    ax2.plot(products, prices, 'b-')
    ax1.set_xlabel('Product Name')
    ax1.set_ylabel('Quantity Ordered', color='green')
    ax2.set_ylabel('Price ($)', color='b')
    ax1.set_xticklabels(products, rotation='vertical', size=8)


split_product()
set_bar_plot_properties()
matplt.show()
