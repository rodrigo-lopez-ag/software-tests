"""Computes the total sales  given two json files"""
import sys
import os
import time
import json


def load_products(file_path: str) -> dict[str, int]:
    """Loads the products from a json file"""
    catalogue = {}
    with open(file_path, 'r', encoding='utf-8') as file_content:
        json_file_content = json.load(file_content)
        for item in json_file_content:
            catalogue[item['title']] = item['price']
    return catalogue


def load_sales(file_path: str) -> list[tuple[str, int]]:
    """Loads the sales from a json file"""
    sales = []
    with open(file_path, 'r', encoding='utf-8') as file_content:
        json_file_content = json.load(file_content)
        for item in json_file_content:
            tup = (item['Product'], item['Quantity'])
            sales.append(tup)
    return sales


def calculate_total_sales(catalogue: dict[str, int],
                          sales: list[tuple[str, int]]) -> int:
    """Calculates the total sum of sales"""
    total = 0
    for item in sales:
        try:
            total += catalogue[item[0]] * item[1]
        except KeyError:
            total += 0
    return total


def create_file(file_path: str, write_results: str, delta_time: float) -> None:
    """Creates a file with the same results shown in the terminal"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f'Total sales sum was: {write_results}\n')
        file.write(f'Execution time was: {round(delta_time, 4)}')


if len(sys.argv) > 2:
    catalogue_path = sys.argv[1]
    sales_path = sys.argv[2]
    if (os.path.isfile(catalogue_path) and os.path.exists(catalogue_path))\
       and (os.path.isfile(sales_path) and os.path.exists(sales_path)):
        startTime = time.time()
        products = load_products(catalogue_path)
        product_sales = load_sales(sales_path)
        total_sales = round(calculate_total_sales(products, product_sales), 2)
        delta = time.time() - startTime
        print(f'The total sum of sales was: {total_sales}')
        print(f'Total time execution: {round(delta, 4)}')
        create_file('SalesResults.txt', total_sales, delta)
    else:
        print('Something went wrong trying to read the files')
else:
    print('Missing file required. Two json files must be provided\
          a ProductList json and a Sales json')
