import openpyxl
from helper_functions import *


def main():
    inv_file = openpyxl.load_workbook('inventory.xlsx')
    product_list = inv_file['Sheet1']
    print(f'Total Products per supplier in the sheet are {get_product_per_supplier(product_list)}')
    print(f'Total amount to be paid per supplier are  {get_amount_per_supplier(product_list)}')
    print(
        f'Products number going out of stock soon with their inventory count are  '
        f'{get_inventory_less_than(10, product_list)}')
    # write new excel file with total amount
    write_total_inventory_worth(inv_file, product_list)


main()
