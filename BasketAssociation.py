import pandas as pd
import os
import re


def read_file(path):
    df = pd.read_excel(path + "Socom1.xlsx")
    for i in os.listdir(path)[1:]:
        df2 = pd.read_excel(path + i)
        df = pd.concat([df, df2])
    return df


def get_products_file(df):
    products = df[['Đơn hàng', 'Sản phẩm']]
    products.rename(columns={'Đơn hàng': 'OrderID', 'Sản phẩm': 'Product'}, inplace=True)
    products['OrderID'] = products['OrderID'].astype('Int64')
    products['ProductType'] = products['Product'].astype(str).apply(
        lambda x: ' '.join(x.split()[:3]) if len(x.split()) >= 3 else "ELSE")
    products = products[['OrderID', 'ProductType']]
    products = products[~products['ProductType'].str.contains(r'(?i)\[Quà tặng\]', regex=True, na=False)]
    products = products[~products['ProductType'].str.contains(r'(?i)\[Gift\]', regex=True, na=False)]
    products = products[~products['ProductType'].str.contains(r'^ELSE$', regex=True, na=False)]
    return products


def concatenate_product_types(product_types):
    return '-'.join(product_types)


def get_combo(products):
    products['ItemNumber'] = products.groupby('OrderID')['ProductType'].cumcount() + 1
    products = products[products['ItemNumber'] <= 2]
    return products.pivot_table(index='OrderID', values='ProductType', aggfunc=concatenate_product_types).value_counts()


def main():
    path = "C:\\Bi\\Win Backup\\LongDA\\Lvl2\\Class8 FIFO\\Basket Association\\"
    print("Reading file from Path")
    df = read_file(path)
    print("Getting products information")
    products = get_products_file(df)
    print("Generating Combo report")
    return print(get_combo(products))


if __name__ == "__main__":
    main()

