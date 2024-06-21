def get_product_per_supplier(product_list):
    product_per_supplier = {}
    for product_row in range(2, product_list.max_row + 1):
        supplier_name = product_list.cell(product_row, 4).value
        if supplier_name in product_per_supplier:
            product_per_supplier[supplier_name] += 1
        else:
            product_per_supplier[supplier_name] = 1
    return product_per_supplier


def get_amount_per_supplier(product_list):
    amount_per_supplier = {}
    for product_row in range(2, product_list.max_row + 1):
        supplier_name = product_list.cell(product_row, 4).value
        inventory = product_list.cell(product_row, 2).value
        price = product_list.cell(product_row, 3).value
        if supplier_name in amount_per_supplier:
            amount_per_supplier[supplier_name] += inventory * price
        else:
            amount_per_supplier[supplier_name] = inventory * price
    return amount_per_supplier


def get_inventory_less_than(amount, product_list):
    product_under = {}
    for product_row in range(2, product_list.max_row + 1):
        product_no = int(product_list.cell(product_row, 1).value)
        inventory = int(product_list.cell(product_row, 2).value)
        if inventory < amount:
            product_under[product_no] = inventory
    return product_under


def write_total_inventory_worth(inv_file, product_list):
    for product_row in range(2, product_list.max_row + 1):
        inventory_worth = product_list.cell(product_row, 5)
        inventory = product_list.cell(product_row, 2).value
        price = product_list.cell(product_row, 3).value
        inventory_worth.value = inventory * price
    inv_file.save('inventory_total.xlsx')
